# Practical 1 - Explore the dataset using descriptive statistic
# EASY GENERALIZED DATASET EXPLORATION CODE
# Works for most CSV datasets

import pandas as pd
import matplotlib.pyplot as plt

# 1. LOAD DATASET
df = pd.read_csv(
    "/content/Retail Intelligence dataset.csv"
)  # replace with your file name

# 2. DISPLAY FIRST 5 ROWS
print("\nFirst 5 Rows")
print(df.head())

# 3. DATASET INFORMATION
print("\nDataset Info")
print(df.info())

# 4. CHECK MISSING VALUES
print("\nMissing Values")
print(df.isnull().sum())

# 5. DESCRIPTIVE STATISTICS
print("\nDescriptive Statistics")
print(df.describe())

# 6. COLUMN NAMES
print("\nColumn Names")
print(df.columns)

# 7. VALUE COUNTS FOR A COLUMN
# Replace 'column_name' with any categorical column
print("\nValue Counts")
print(df["City"].value_counts())

# 8. HISTOGRAM
# Replace 'numeric_column' with any numeric column
df["Age"].hist()

plt.title("Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()

# 9. PIE CHART
# Replace 'column_name' with categorical column
df["Membership_Tier"].value_counts().plot.pie(autopct="%1.1f%%")

plt.title("Pie Chart")
plt.ylabel("")
plt.show()


# Practical 2 - Explore the dataset using inferential statistic
import pandas as pd
from scipy.stats import ttest_ind

# LOAD DATASET
df = pd.read_csv("/content/Retail Intelligence dataset.csv")

# CREATE TWO GROUPS
male = df[df["Gender"] == "M"]["Final_Amount"]
female = df[df["Gender"] == "F"]["Final_Amount"]

# T-TEST
t_stat, p_value = ttest_ind(male, female)

# OUTPUT
print("T-Statistic:", t_stat)
print("P-Value:", p_value)

# INTERPRETATION
if p_value < 0.05:
    print("Significant Difference")
else:
    print("No Significant Difference")


# Practical 3 - Apply data cleaning techniques
# GENERAL DATA PREPROCESSING CODE
# RUN THIS FIRST FOR ANY DATASET

import pandas as pd

# LOAD DATASET
df = pd.read_csv(
    "/content/Retail Intelligence dataset.csv"
)  # replace with your file name

# -------------------------------
# BASIC DATASET INFORMATION
# -------------------------------

print("\nFIRST 5 ROWS")
print(df.head())

print("\nDATASET INFO")
print(df.info())

print("\nCOLUMN NAMES")
print(df.columns)

print("\nDATASET SHAPE")
print(df.shape)

# -------------------------------
# CHECK MISSING VALUES
# -------------------------------

print("\nMISSING VALUES")
print(df.isnull().sum())

# -------------------------------
# REMOVE DUPLICATES
# -------------------------------

df.drop_duplicates(inplace=True)

print("\nDUPLICATES REMOVED")

# -------------------------------
# HANDLE MISSING VALUES
# -------------------------------

# NUMERIC COLUMNS → MEAN IMPUTATION
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns

for col in numeric_cols:
    df[col].fillna(df[col].mean(), inplace=True)

# CATEGORICAL COLUMNS → MODE IMPUTATION
categorical_cols = df.select_dtypes(include=["object"]).columns

for col in categorical_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)

# -------------------------------
# FINAL CHECK
# -------------------------------

print("\nMISSING VALUES AFTER CLEANING")
print(df.isnull().sum())

print("\nPREPROCESSING COMPLETED")


# Practical 4 - Apply data visualization techniques to explore data
# GENERAL DATA VISUALIZATION PROGRAM
# WORKS FOR MOST DATASETS

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# LOAD DATASET
df = pd.read_csv(
    "/content/Retail Intelligence dataset.csv"
)  # replace with your file name

# -------------------------------
# DATASET INFO
# -------------------------------

print(df.head())

print(df.info())

# -------------------------------
# HISTOGRAM
# NUMERIC COLUMN
# -------------------------------

df["Age"].hist()

plt.title("Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")

plt.show()

# -------------------------------
# PIE CHART
# CATEGORICAL COLUMN
# -------------------------------

df["Product_Category"].value_counts().plot.pie(autopct="%1.1f%%")

plt.title("Pie Chart")
plt.ylabel("")

plt.show()

# -------------------------------
# BAR CHART
# CATEGORICAL COLUMN
# -------------------------------

df["Payment_Mode"].value_counts().plot(kind="bar")

plt.title("Bar Chart")
plt.xlabel("Category")
plt.ylabel("Count")

plt.show()

# -------------------------------
# SCATTER PLOT
# TWO NUMERIC COLUMNS
# -------------------------------

plt.scatter(df["Quantity"], df["Final_Amount"])

plt.title("Scatter Plot")
plt.xlabel("Quantity")
plt.ylabel("Final_Amount")

plt.show()

# -------------------------------
# HEATMAP
# CORRELATION BETWEEN NUMERIC COLUMNS
# -------------------------------

corr = df.corr(numeric_only=True)

sns.heatmap(corr, annot=True)

plt.title("Heatmap")

plt.show()


# Practical 5 - Implement and explore performance evaluation metrics for Data Models (supervised/unsupervised learning)
# GENERALIZED SUPERVISED LEARNING PROGRAM
# WITH ACCURACY, PRECISION, RECALL, F1-SCORE

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score

# -------------------------------
# LOAD DATASET
# -------------------------------

df = pd.read_csv("/content/Retail Intelligence dataset.csv")  # replace file name

# -------------------------------
# SELECT FEATURES
# -------------------------------

X = df[
    ["Final_Amount", "Purchase_Hour", "Geo_Distance_From_Home_km"]
]  # replace with input columns

# -------------------------------
# SELECT TARGET COLUMN
# -------------------------------

y = df["Fraud_Label"]  # replace with output column

# -------------------------------
# TRAIN TEST SPLIT
# -------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------------------
# CREATE MODEL
# -------------------------------

model = LogisticRegression()

# -------------------------------
# TRAIN MODEL
# -------------------------------

model.fit(X_train, y_train)

# -------------------------------
# PREDICTION
# -------------------------------

y_pred = model.predict(X_test)

# -------------------------------
# PERFORMANCE EVALUATION
# -------------------------------

accuracy = accuracy_score(y_test, y_pred)

precision = precision_score(y_test, y_pred)

recall = recall_score(y_test, y_pred)

f1 = f1_score(y_test, y_pred)

# -------------------------------
# PRINT RESULTS
# -------------------------------

print("Accuracy:", accuracy)

print("Precision:", precision)

print("Recall:", recall)

print("F1 Score:", f1)


# Practical 6 - Implement SMOTE technique to generate synthetic data and implement outlier detection using distance based/density based method
from imblearn.over_sampling import SMOTE

smote = SMOTE(random_state=42)

X_resampled, y_resampled = smote.fit_resample(X, y)

print(y_resampled.value_counts())

smote_df = pd.concat([X_resampled, y_resampled], axis=1)
smote_df.to_csv("smote_dataset.csv", index=False)

from sklearn.neighbors import LocalOutlierFactor

lof = LocalOutlierFactor()

df["Outlier"] = lof.fit_predict(df[["Geo_Distance_From_Home_km"]])

print(df["Outlier"])


# Practical 7 - Perform feature engineering and feature selection on a given dataset and study its impact on supervised learning model performance
# FEATURE ENGINEERING + FEATURE SELECTION
# COMPARING MODEL PERFORMANCE

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# ------------------------------------------------
# LOAD DATASET
# ------------------------------------------------

df = pd.read_csv("/content/Retail Intelligence dataset.csv")  # replace file name

# =====================================================
# BEFORE FEATURE ENGINEERING & FEATURE SELECTION
# =====================================================

# BASIC FEATURES

X1 = df[["Age", "Annual_Income"]]

# TARGET

y = df["Fraud_Label"]

# TRAIN TEST SPLIT

X_train1, X_test1, y_train1, y_test1 = train_test_split(
    X1, y, test_size=0.2, random_state=42
)

# MODEL

model1 = LogisticRegression(class_weight="balanced")

# TRAIN

model1.fit(X_train1, y_train1)

# PREDICT

y_pred1 = model1.predict(X_test1)

# ACCURACY

accuracy_before = accuracy_score(y_test1, y_pred1)

print("Accuracy Before Feature Engineering & Feature Selection:", accuracy_before)

# =====================================================
# FEATURE ENGINEERING
# =====================================================

# CREATE NEW FEATURE

df["Average_Price"] = df["Final_Amount"] / df["Quantity"]

# =====================================================
# AFTER FEATURE ENGINEERING & FEATURE SELECTION
# =====================================================

# SELECT BETTER FEATURES

X2 = df[["Final_Amount", "Purchase_Hour", "Geo_Distance_From_Home_km", "Average_Price"]]

# TRAIN TEST SPLIT

X_train2, X_test2, y_train2, y_test2 = train_test_split(
    X2, y, test_size=0.2, random_state=42
)

# MODEL

model2 = LogisticRegression(class_weight="balanced")

# TRAIN

model2.fit(X_train2, y_train2)

# PREDICT

y_pred2 = model2.predict(X_test2)

# ACCURACY

accuracy_after = accuracy_score(y_test2, y_pred2)

print("Accuracy After Feature Engineering & Feature Selection:", accuracy_after)


# Practical 8 - Implement time series forecasting
# SIMPLE TIME SERIES FORECASTING PROGRAM

import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------
# LOAD DATASET
# --------------------------------

df = pd.read_csv("/content/Retail Intelligence dataset.csv")  # replace file name

# --------------------------------
# CONVERT DATE COLUMN
# --------------------------------

df["Date"] = pd.to_datetime(df["Date"])

# --------------------------------
# SORT DATA BY DATE
# --------------------------------

df = df.sort_values("Date")

# --------------------------------
# SET DATE AS INDEX
# --------------------------------

df.set_index("Date", inplace=True)

# --------------------------------
# MOVING AVERAGE FORECASTING
# --------------------------------

df["Forecast"] = df["Final_Amount"].rolling(window=3).mean()

# --------------------------------
# DISPLAY DATA
# --------------------------------

print(df[["Final_Amount", "Forecast"]])

# --------------------------------
# PLOT GRAPH
# --------------------------------

plt.plot(df.index, df["Final_Amount"], label="Original Data")

plt.plot(df.index, df["Forecast"], label="Forecast")

plt.xlabel("Date")
plt.ylabel("Values")

plt.title("Time Series Forecasting")

plt.legend()

plt.show()


# Practical 9,10 - Demonstrate data science lifecycle
# DATA SCIENCE LIFE CYCLE PROGRAM
# GENERIC PROGRAM FOR ANY DATASET

# =====================================================
# IMPORT LIBRARIES
# =====================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# =====================================================
# 1. DATA COLLECTION
# =====================================================

# LOAD DATASET

df = pd.read_csv("/content/Retail Intelligence dataset.csv")  # replace file name

print("FIRST 5 ROWS")
print(df.head())

# =====================================================
# 2. DATA PREPROCESSING
# =====================================================

# CHECK MISSING VALUES

print("\nMISSING VALUES")
print(df.isnull().sum())

# REMOVE DUPLICATES

df.drop_duplicates(inplace=True)

# HANDLE NUMERIC MISSING VALUES

numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns

for col in numeric_cols:
    df[col] = df[col].fillna(df[col].mean())

# HANDLE CATEGORICAL MISSING VALUES

categorical_cols = df.select_dtypes(include=["object"]).columns

for col in categorical_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

print("\nPREPROCESSING COMPLETED")

# =====================================================
# 3. EXPLORATORY DATA ANALYSIS
# =====================================================

# HISTOGRAM

df["Final_Amount"].hist()

plt.title("Histogram")

plt.show()

# PIE CHART

df["Membership_Tier"].value_counts().plot.pie(autopct="%1.1f%%")

plt.title("Pie Chart")

plt.ylabel("")

plt.show()

# =====================================================
# 4. FEATURE ENGINEERING
# =====================================================

# CREATE NEW FEATURE

df["New_Feature"] = df["Final_Amount"] / df["Quantity"]

print("\nFEATURE ENGINEERING COMPLETED")

# =====================================================
# 5. FEATURE SELECTION
# =====================================================

X = df[["Final_Amount", "Quantity", "New_Feature"]]

y = df["Fraud_Label"]

# =====================================================
# 6. MODEL BUILDING
# =====================================================

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression(class_weight="balanced")

model.fit(X_train, y_train)

# =====================================================
# 7. MODEL EVALUATION
# =====================================================

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\nMODEL ACCURACY:", accuracy)

# =====================================================
# 8. VISUALIZATION
# =====================================================

sns.boxplot(x=df["Final_Amount"])

plt.title("Boxplot")

plt.show()

print("\nDATA SCIENCE LIFE CYCLE COMPLETED")
