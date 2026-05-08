import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterswarnings("ignore")

# ml and preprocessing
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StanderdScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# models & evaluation
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import IsolationForest
from sklearn.metrics import (
    mean_squared_error,
    r2_score,
    accuracy_score,
    classification_report,
)

# smote & time series
from imblearn.over_sampling import SMOTE
from statsmodels.tsa.arima.model import ARIMA


# 1. configuration

FILE_PATH = "/content/Bank_Transactions.csv"
TARGET_COL = "Fraud_Label"
TASK_TYPE = "classification"

# optional
DATE_COL = "Date"  # datetime column for time series
TS_TARGET = "Amount"  # which column to forecast over time

# 2 LOAD DATA & AUTO-DETECT COLUMNS
print("--- Loading Data & Exploring ---")
df = pd.read_csv(FILE_PATH)

print(df.info())
print("\nDescriptive Statistics:\n", df.describe())

# Auto-detect column types
num_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
cat_cols = df.select_dtype(include=["object", "category"]).columns.tolist()

# Remove target and date columns from feature lists so they don't get processed normally

for col_list in [num_cols, cat_cols]:
    if TARGET_COL in col_list:
        col_list.remove(TARGET_COL)
    if DATE_COL and DATE_COL in col_list:
        col_list.remove(DATE_COL)

# 3 anomaly detection
print("\n--- Running Anomaly Detection ---")
# we use isolation forest to find weird, outlier data points in our numerical columns
iso_forest = IsolationForest(contamination=0.05, random_state=42)
# assumes 5% anomalies
df["Is_Anomaly"] = iso_forest.fit_predict(df[num_cols].fillna(df[num_cols].median()))

# plotting the anomalies
plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df, x=num_cols[0], y=num_cols[1], hue="Is_Anomaly", palette="coolwarm"
)
plt.title(f"Anomaly Detection: -1 indicates Anomalies")
plt.show()

# remove anomalies from the dataset before training our main model
df = df[df["Is_Anomaly"] == 1].drop(colums=["Is_Anomaly"])

# 4 data visualization
print("\n--- Generating Business Visualizations ---")

plt.figure(figsize=(6, 4))
if TASK_TYPE == "classification":
    sns.countplot(data=df, x=TARGET_COL)
else:
    sns.histplot(data=df, x=TARGET_COL, kde=True)
plt.title(f"Distribution of {TARGET_COL}")
plt.show()

if len(num_cols) > 1:
    plt.figure(figsize=(10, 8))
    sns.heatmap(df[num_cols].corr(), annot=True, cmap="Blues", fmt=".2f")
    plt.title("Correlation Matrix of Numerical Features")
    plt.show()


if len(num_cols) > 0:
    plt.figure(figsize=(6, 4))
    sns.boxplot(data=df, y=num_cols[0], color="lightblue")
    plt.title(f"Univariate analysis: spread of {num_cols}")
    plt.ylable(num_cols[0])
    plt.show()

if len(num_cols) >= 2:
    plt.figure(figsize=(8, 5))
    sns.scatterplot(
        data=df,
        x=num_cols[0],
        y=num_cols[1],
        hue=TARGET_COL,
        palette="viridis",
        alpha=0.7,
    )
    plt.title(
        f"Multivariate: {num_cols[0]} vs {num_cols[1]} (segmented by {TARGET_COL})"
    )
    plt.show()

if DATE_COL is not None and TS_TARGET in df.columns:
    plt.figure(figsize=(10, 5))
    temp_time_df = df.copy()
    temp_time_df[DATE_COL] = pd.to_datetime(temp_time_df[DATE_COL])

    monthly_trend = temp_time_df.groupby(temp_time_df[DATE_COL].dt.to_period("M"))[
        TS_TARGET
    ].mean()

    monthly_trend.plot(kind="line", marker="o", color="teal")
    plt.title(f"Time-Based Trend: Average {TS_TARGET} per Month")
    plt.ylabel(f"Avg {TS_TARGET}")
    plt.xlabel("Date (Monthly)")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.show()
