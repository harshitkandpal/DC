import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings("ignore")

# ML & Preprocessing
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Models & Evaluation
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import IsolationForest
from sklearn.metrics import (
    mean_squared_error,
    r2_score,
    accuracy_score,
    classification_report,
)

# SMOTE & Time Series
from imblearn.over_sampling import SMOTE
from statsmodels.tsa.arima.model import ARIMA

# ==========================================
# 1. CONFIGURATION (CHANGE THESE TOMORROW)
# ==========================================
FILE_PATH = "/content/Bank_Transactions.csv"
TARGET_COL = "Fraud_Label"
TASK_TYPE = "classification"  # Choose 'classification' or 'regression'

# Optional: Set to None if not asked
DATE_COL = "Date"  # Datetime column for time series
TS_TARGET = "Amount"  # Which numerical column to forecast over time

# ==========================================
# 2. LOAD DATA & AUTO-DETECT COLUMNS
# ==========================================
print("--- Loading Data & Exploring ---")
df = pd.read_csv(FILE_PATH)

print(df.info())
print("\nDescriptive Statistics:\n", df.describe())

# Auto-detect column types (saves you time!)
num_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
cat_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()

# Remove target and date columns from feature lists so they don't get processed normally
for col_list in [num_cols, cat_cols]:
    if TARGET_COL in col_list:
        col_list.remove(TARGET_COL)
    if DATE_COL and DATE_COL in col_list:
        col_list.remove(DATE_COL)

# ==========================================
# 3. ANOMALY DETECTION
# ==========================================
print("\n--- Running Anomaly Detection ---")
# We use Isolation Forest to find weird, outlier data points in our numerical columns
iso_forest = IsolationForest(
    contamination=0.05, random_state=42
)  # Assumes 5% anomalies
df["Is_Anomaly"] = iso_forest.fit_predict(df[num_cols].fillna(df[num_cols].median()))

# Plotting the anomalies (Business Insight: "We identified X% of transactions as highly unusual, which could indicate fraud or system errors that require immediate audit.")
plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df, x=num_cols[0], y=num_cols[1], hue="Is_Anomaly", palette="coolwarm"
)
plt.title(f"Anomaly Detection: -1 indicates Anomalies")
plt.show()

# Remove anomalies from the dataset before training our main model
df = df[df["Is_Anomaly"] == 1].drop(columns=["Is_Anomaly"])

# ==========================================
# 4. DATA VISUALIZATION (BUSINESS INSIGHTS)
# ==========================================
print("\n--- Generating Business Visualizations ---")

# VIZ 1: Target Distribution
# Insight for Examiner: "This shows our current business balance. If one class is too low, we are losing visibility on that customer segment."
plt.figure(figsize=(6, 4))
if TASK_TYPE == "classification":
    sns.countplot(data=df, x=TARGET_COL)
else:
    sns.histplot(data=df, x=TARGET_COL, kde=True)
plt.title(f"Distribution of {TARGET_COL}")
plt.show()

# VIZ 2: Correlation Heatmap
# Insight for Examiner: "We can see which factors drive our target. For example, feature X is highly correlated with feature Y, meaning we might be able to cut costs by only tracking one of them."
plt.figure(figsize=(10, 8))
sns.heatmap(df[num_cols].corr(), annot=True, cmap="Blues", fmt=".2f")
plt.title("Correlation Matrix of Numerical Features")
plt.show()

# ==========================================
# 5. TIME SERIES FORECASTING (If applicable)
# ==========================================
if DATE_COL is not None and TS_TARGET in df.columns:
    print("\n--- Running Time Series Forecasting ---")

    # Prepare time series data
    ts_df = df.copy()
    ts_df[DATE_COL] = pd.to_datetime(ts_df[DATE_COL])
    ts_df = ts_df.set_index(DATE_COL).sort_index()

    # Resample to monthly ('M') average to smooth out noise
    monthly_data = ts_df[TS_TARGET].resample("M").mean().dropna()

    # Fit a basic ARIMA model (Auto-Regressive Integrated Moving Average)
    try:
        ts_model = ARIMA(monthly_data, order=(1, 1, 1))  # Basic baseline parameters
        ts_results = ts_model.fit()
        forecast = ts_results.forecast(steps=6)  # Forecast next 6 months

        # Plotting the Forecast
        # Insight for Examiner: "Based on historical trends, we project these values for the next 6 periods. The business should adjust inventory/staffing accordingly."
        plt.figure(figsize=(10, 5))
        plt.plot(monthly_data.index, monthly_data, label="Historical Data")
        plt.plot(
            pd.date_range(monthly_data.index[-1], periods=7, freq="M")[1:],
            forecast,
            color="red",
            label="6-Month Forecast",
        )
        plt.title(f"{TS_TARGET} Forecast")
        plt.legend()
        plt.show()
    except Exception as e:
        print(f"Time series couldn't fit (likely too little data): {e}")

# ==========================================
# 6. PREPROCESSING & PIPELINE
# ==========================================
print("\n--- Preprocessing & Modeling ---")
X = df.drop(columns=[TARGET_COL])
if DATE_COL is not None:
    X = X.drop(columns=[DATE_COL], errors="ignore")  # Drop dates for standard ML

y = df[TARGET_COL]

# Split data FIRST
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Build Preprocessor
preprocessor = ColumnTransformer(
    transformers=[
        (
            "num",
            Pipeline(
                [
                    ("imputer", SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler()),
                ]
            ),
            num_cols,
        ),
        (
            "cat",
            Pipeline(
                [
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    (
                        "onehot",
                        OneHotEncoder(handle_unknown="ignore", sparse_output=False),
                    ),
                ]
            ),
            cat_cols,
        ),
    ]
)

# Fit and transform
X_train_processed = preprocessor.fit_transform(X_train)
X_test_processed = preprocessor.transform(X_test)

# ==========================================
# 7. SMOTE & MODELING
# ==========================================
if TASK_TYPE == "classification":
    print("Task: Classification. Applying SMOTE and Decision Tree...")
    # Apply SMOTE only to training data
    smote = SMOTE(random_state=42)
    X_train_final, y_train_final = smote.fit_resample(X_train_processed, y_train)

    # Train Model
    model = DecisionTreeClassifier(max_depth=5, random_state=42)
    model.fit(X_train_final, y_train_final)

    # Evaluate
    preds = model.predict(X_test_processed)
    print("Accuracy:", accuracy_score(y_test, preds))
    print("\nClassification Report:\n", classification_report(y_test, preds))

elif TASK_TYPE == "regression":
    print("Task: Regression. Skipping SMOTE. Applying Linear Regression...")
    # Regression cannot use SMOTE
    X_train_final, y_train_final = X_train_processed, y_train

    # Train Model
    model = LinearRegression()
    model.fit(X_train_final, y_train_final)

    # Evaluate
    preds = model.predict(X_test_processed)
    print("RMSE:", np.sqrt(mean_squared_error(y_test, preds)))
    print("R2 Score:", r2_score(y_test, preds))
