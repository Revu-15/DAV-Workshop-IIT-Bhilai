# Data Science Workshop: Day 1 – Foundations: Loading, Cleaning & Preprocessing

Welcome to Day 1 of the Data Science Workshop! This session focuses on the foundational skills of loading, cleaning, and preprocessing data using Python and Pandas. Below is a detailed guide covering all topics from the Day 1 schedule, including explanations, code examples, and hands-on activities. By the end of this session, you’ll be equipped to handle real-world datasets effectively.

---


---
Live from link for today's Hands-On notebook submissions:
[Google-Form](https://docs.google.com/forms/d/e/1FAIpQLSdWEIULoHcL6gsdSQ0YwukuqNgxHajVsOAmPUgrc4B28ZA23Q/viewform?usp=dialog)
---
## Pre-Lunch Session

### 1. Environment Setup
To ensure a smooth workshop experience, set up your Python environment using either **Anaconda** (recommended for simplicity) or **pip** to manage dependencies. Both methods include necessary libraries (Pandas, NumPy, etc.) for data science tasks.

#### Option 1: Using Anaconda
Anaconda simplifies dependency management and ensures compatibility across libraries, making it ideal for data science workflows.

**Steps:**
1. **Install Anaconda:**
   - Download and install Anaconda from [anaconda.com](https://www.anaconda.com/products/distribution).
   - Follow the installation instructions for your operating system (Windows, macOS, or Linux).
2. **Create a Virtual Environment:**
   ```bash
   conda create -n ds_workshop python=3.9 pandas numpy jupyter openpyxl sqlalchemy
   conda activate ds_workshop
   ```
3. **Clone the Workshop Repository:**
   - Clone the workshop materials from the provided GitHub repository (replace with your repo URL):
     ```bash
     git clone <repository-url>
     cd <repository-folder>
     ```
4. **Verify Pandas Installation:**
   - Open a Jupyter Notebook and run:
     ```python
     import pandas as pd
     print(pd.__version__)
     ```
   - Ensure Pandas is installed (version 2.0+ recommended).

#### Option 2: Using pip
If you prefer using Python’s native package manager, you can set up your environment with `pip`.

**Steps:**
1. **Install Python:**
   - Ensure Python 3.9+ is installed from [python.org](https://www.python.org/downloads/).
2. **Create a Virtual Environment:**
   ```bash
   python -m venv ds_workshop
   source ds_workshop/bin/activate  # On Windows: ds_workshop\Scripts\activate
   ```
3. **Install Required Libraries:**
   ```bash
   pip install pandas numpy jupyter openpyxl sqlalchemy
   ```
4. **Clone the Workshop Repository:**
   - Same as above:
     ```bash
     git clone <repository-url>
     cd <repository-folder>
     ```
5. **Verify Pandas Installation:**
   - Open a Jupyter Notebook (`jupyter notebook`) and run:
     ```python
     import pandas as pd
     print(pd.__version__)
     ```

#### Why Choose Anaconda or pip?
- **Anaconda:** Preferred for beginners due to its pre-configured environment and dependency management.
- **pip:** Lightweight and suitable for users comfortable with manual dependency management.

---

### 2. Pandas Basics: Series vs. DataFrame
Pandas is a powerful Python library for data manipulation and analysis. It provides two primary data structures:
- **Series:** A one-dimensional array-like object that holds data of any type (e.g., integers, strings).
- **DataFrame:** A two-dimensional table with rows and columns, similar to a spreadsheet.

#### Example Code:
```python
import pandas as pd

# Creating a Series
series = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print("Series:\n", series)

# Creating a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)
print("\nDataFrame:\n", df)
```

**Key Difference:**
- A **Series** is like a single column, while a **DataFrame** is a collection of columns with shared indices.
- Use Series for single-variable analysis; use DataFrames for tabular data.

---

### 3. Data I/O: CSV, Excel, JSON, SQL
Pandas supports reading and writing data in multiple formats, making it versatile for real-world datasets.

#### Supported Formats and Methods:
- **CSV:** `pd.read_csv()`, `df.to_csv()`
- **Excel:** `pd.read_excel()`, `df.to_excel()` (requires `openpyxl`)
- **JSON:** `pd.read_json()`, `df.to_json()`
- **SQL:** `pd.read_sql()`, `df.to_sql()` (requires `sqlalchemy`)

#### Example Code:
```python
import pandas as pd
import sqlite3

# Reading a CSV file
csv_df = pd.read_csv('____.csv')

# Reading an Excel file
excel_df = pd.read_excel('____.xlsx', sheet_name='Sheet1')

# Reading a JSON file
json_df = pd.read_json('____.json')

# Reading from an SQL database
conn = sqlite3.connect('____.db')
sql_df = pd.read_sql('SELECT * FROM table_name', conn)

# Writing to CSV
csv_df.to_csv('____.csv', index=False)
```

**Note:** Ensure required libraries (`openpyxl`, `sqlalchemy`) are installed via `conda` or `pip`.

---

### 4. Performance Tips: dtype, usecols, chunksize
Efficient data loading can save time and memory, especially with large datasets.

#### Key Techniques:
- **dtype:** Specify column data types to reduce memory usage (e.g., use `int8` instead of `int64` for small integers).
- **usecols:** Load only specific columns to avoid unnecessary data.
- **chunksize:** Process large files in chunks to prevent memory overload.

#### Example Code:
```python
import pandas as pd

# Specify dtypes to optimize memory
dtypes = {'id': 'int32', 'name': 'string', 'score': 'float32'}
df = pd.read_csv('____.csv', dtype=dtypes, usecols=['id', 'name', 'score'])

# Process large CSV in chunks
for chunk in pd.read_csv('____.csv', chunksize=1000):
    # Process each chunk (e.g., filter, aggregate)
    print(chunk.shape)
```

**Why It Matters:** Optimizing data types and loading strategies can reduce memory usage by up to 90% and speed up processing significantly.

---

### 5. Hands-On: Load and Inspect Open-Source Dataset
**Task:** Load and explore an open-source dataset (e.g., a publicly available dataset).

#### Steps:
1. Download an open-source dataset (e.g., from Kaggle) as a CSV file.
2. Load the dataset using Pandas.
3. Inspect the data using methods like `.head()`, `.info()`, and `.describe()`.

#### Example Code:
```python
import pandas as pd

# Load dataset
df = pd.read_csv('____.csv')

# Inspect first 5 rows
print(df.head())

# Check data types and missing values
print(df.info())

# Summary statistics
print(df.describe())
```

**Expected Output:**
- `.head()`: Displays the first 5 rows.
- `.info()`: Shows column names, data types, and missing value counts.
- `.describe()`: Provides statistical summaries (mean, min, max, etc.) for numerical columns.

---

## Post-Lunch Session

### 1. Missing Data: Drop vs. Impute
Missing data is common in real-world datasets and must be handled carefully to avoid biased analyses. There are two primary strategies: dropping missing values or imputing them with substitutes.

#### Dropping Missing Values
Use `dropna()` to remove rows or columns containing missing values. This is effective when missing data is minimal, but excessive dropping can lead to data loss.

**Methods:**
- **Drop rows with any missing values:** Remove rows where at least one value is `NaN`.
- **Drop rows with all missing values:** Remove rows where all values are `NaN`.
- **Drop columns with missing values:** Remove columns with any `NaN` values.
- **Threshold-based dropping:** Drop rows with a minimum number of non-`NaN` values.
- **Subset-based dropping:** Drop rows based on missing values in specific columns.

**Example Code:**
```python
import pandas as pd

# Sample DataFrame with missing values
df = pd.DataFrame({
    'A': [1, None, 3, None, 5],
    'B': [None, 2, None, 4, 5],
    'C': [1, 2, 3, None, None]
})

# Drop rows with any missing values
df_drop_any = df.dropna()

# Drop rows where all values are missing
df_drop_all = df.dropna(how='all')

# Drop columns with any missing values
df_drop_cols = df.dropna(axis=1)

# Drop rows with at least 2 non-NaN values
df_drop_thresh = df.dropna(thresh=2)

# Drop rows with missing values in specific columns
df_drop_subset = df.dropna(subset=['A', 'B'])

print("Drop any:\n", df_drop_any)
print("\nDrop all:\n", df_drop_all)
print("\nDrop columns:\n", df_drop_cols)
print("\nDrop threshold:\n", df_drop_thresh)
print("\nDrop subset:\n", df_drop_subset)
```

**When to Drop:**
- Missing values are less than 5% of the dataset.
- Rows or columns with missing values are not critical to analysis.
- Dropping does not introduce bias (e.g., missing data is random).

#### Imputing Missing Values
Imputation fills missing values with substitutes to preserve data. The choice of method depends on the data type and context.

**Methods:**
- **Mean/Median/Mode Imputation:** Replace missing values with the column’s mean (numerical), median (numerical), or mode (categorical).
- **Constant Imputation:** Fill with a fixed value (e.g., 0 or 'Unknown').
- **Forward/Backward Fill:** Propagate the next or previous value (useful for time-series data).
- **Interpolation:** Estimate missing values based on surrounding data (e.g., linear interpolation).
- **K-Nearest Neighbors (KNN) Imputation:** Use values from similar rows (requires `scikit-learn`).
- **Predictive Imputation:** Use a machine learning model to predict missing values (advanced).

**Example Code:**
```python
import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer

# Sample DataFrame
df = pd.DataFrame({
    'A': [1, None, 3, None, 5],
    'B': [None, 2, None, 4, 5],
    'C': ['X', 'Y', None, 'Z', None]
})

# Mean imputation for numerical column
df_mean = df.copy()
df_mean['A'] = df_mean['A'].fillna(df_mean['A'].mean())

# Median imputation
df_median = df.copy()
df_median['A'] = df_median['A'].fillna(df_median['A'].median())

# Mode imputation for categorical column
df_mode = df.copy()
df_mode['C'] = df_mode['C'].fillna(df_mode['C'].mode()[0])

# Constant imputation
df_constant = df.copy()
df_constant['B'] = df_constant['B'].fillna(0)

# Forward fill
df_ffill = df.copy()
df_ffill['A'] = df_ffill['A'].ffill()

# Linear interpolation
df_interp = df.copy()
df_interp['A'] = df_interp['A'].interpolate(method='linear')

# KNN imputation (requires scikit-learn)
knn_imputer = KNNImputer(n_neighbors=2)
df_knn = pd.DataFrame(knn_imputer.fit_transform(df[['A', 'B']]), columns=['A', 'B'])

print("Mean imputation:\n", df_mean)
print("\nMedian imputation:\n", df_median)
print("\nMode imputation:\n", df_mode)
print("\nConstant imputation:\n", df_constant)
print("\nForward fill:\n", df_ffill)
print("\nInterpolation:\n", df_interp)
print("\nKNN imputation:\n", df_knn)
```

**When to Impute:**
- Data loss from dropping is unacceptable (e.g., >5% missing).
- Missing values follow a pattern that can be reasonably estimated.
- Domain knowledge supports a specific imputation method (e.g., median for skewed data).

**Caution:** Imputation can introduce bias if not done carefully. Always validate the impact on your analysis.

---

### 2. Outliers: IQR, Z-score
Outliers can skew analyses and must be detected and handled appropriately.

#### Detection Methods:
- **IQR (Interquartile Range):** Identify values outside 1.5 * IQR from Q1 and Q3.
- **Z-score:** Flag values with a Z-score > 3 (far from the mean).

#### Example Code:
```python
import pandas as pd
import numpy as np

# Sample DataFrame
df = pd.DataFrame({'values': [1, 2, 3, 100, 4, 5, 200]})

# IQR method
Q1 = df['values'].quantile(0.25)
Q3 = df['values'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers_iqr = df[(df['values'] < lower_bound) | (df['values'] > upper_bound)]

# Z-score method
df['z_score'] = (df['values'] - df['values'].mean()) / df['values'].std()
outliers_z = df[abs(df['z_score']) > 3]

print("IQR Outliers:\n", outliers_iqr)
print("\nZ-score Outliers:\n", outliers_z)
```

**Handling Outliers:** Remove, cap, or transform outliers based on domain knowledge.

---

### 3. Type Conversion & Date Handling
Correct data types ensure accurate computations, and proper date handling is critical for time-series analysis.

#### Type Conversion
Converting columns to appropriate types (e.g., `int`, `float`, `category`) optimizes memory and enables specific operations. Common methods include `astype()`, `to_numeric()`, and `pd.Categorical`.

**Methods:**
- **astype():** Convert to a specific type (e.g., `int`, `float`, `str`, `category`).
- **to_numeric():** Convert to numeric types, handling non-numeric values (e.g., coerce to `NaN`).
- **pd.Categorical():** Convert to categorical type for ordinal or nominal data.
- **to_datetime():** Convert to datetime for date/time operations.
- **str methods:** Convert to string and apply string operations (e.g., `.str.lower()`).
- **Custom mapping:** Use `.map()` or `.replace()` for specific value conversions.

**Example Code:**
```python
import pandas as pd
import numpy as np

# Sample DataFrame
df = pd.DataFrame({
    'id': ['1', '2', 'abc', '4'],
    'score': ['10.5', '20.7', '30.2', None],
    'category': ['low', 'high', 'medium', 'low'],
    'status': [True, False, True, False],
    'text': ['Apple', 'BANANA', 'cherry', 'DATE']
})

# Convert to integer with to_numeric (coerce errors to NaN)
df['id'] = pd.to_numeric(df['id'], errors='coerce')

# Convert to float with astype
df['score'] = df['score'].astype('float64')

# Convert to categorical
df['category'] = df['category'].astype('category')

# Convert to boolean
df['status'] = df['status'].astype('bool')

# Convert to string and lowercase
df['text'] = df['text'].astype('str').str.lower()

# Custom mapping for category
df['category_code'] = df['category'].map({'low': 1, 'medium': 2, 'high': 3})

# Convert to ordered categorical
df['category_ordered'] = pd.Categorical(df['category'], categories=['low', 'medium', 'high'], ordered=True)

print(df)
print("\nData types:\n", df.dtypes)
```

**Output Example:**
```
   id  score category  status   text  category_code category_ordered
0  1.0   10.5      low    True  apple              1              low
1  2.0   20.7     high   False banana              3             high
2  NaN   30.2   medium    True cherry              2           medium
3  4.0    NaN      low   False   date              1              low

Data types:
id                   float64
score                float64
category            category
status                  bool
text                  object
category_code        float64
category_ordered    category
dtype: object
```

#### Date Handling
Parse and manipulate dates using `pd.to_datetime()` and extract components (e.g., year, month, day).

**Methods:**
- **pd.to_datetime():** Convert strings to datetime objects.
- **dt accessor:** Extract components like `.dt.year`, `.dt.month`, `.dt.dayofweek`.
- **strptime/strftime:** Parse custom date formats or format dates as strings.
- **resample():** Aggregate time-series data (e.g., daily to monthly).

**Example Code:**
```python
import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    'date': ['2023-01-01', '02/15/2023', '2023-03-31 14:30', 'invalid'],
    'value': [10, 20, 30, 40]
})

# Convert to datetime, coerce invalid values to NaT
df['date'] = pd.to_datetime(df['date'], errors='coerce', format='mixed')

# Extract components
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
df['weekday'] = df['date'].dt.day_name()

# Format dates as strings
df['formatted_date'] = df['date'].dt.strftime('%Y-%m-%d')

# Calculate time differences
df['days_since'] = (pd.to_datetime('2023-12-31') - df['date']).dt.days

print(df)
```

**Output Example:**
```
        date  value    year  month   day   weekday formatted_date  days_since
0 2023-01-01     10  2023.0    1.0   1.0   Sunday    2023-01-01       364.0
1 2023-02-15     20  2023.0    2.0  15.0  Wednesday    2023-02-15       319.0
2 2023-03-31     30  2023.0    3.0  31.0    Friday    2023-03-31       275.0
3        NaT     40     NaN    NaN   NaN      None           NaN         NaN
```

**Why It Matters:** Proper type conversion reduces memory usage and enables accurate computations, while date handling unlocks time-series analysis.

---

### 4. Pipelines: Method Chaining with .pipe()
Pandas’ `.pipe()` method allows you to chain custom functions for cleaner, reusable code.

#### Example Code:
```python
import pandas as pd

# Custom cleaning functions
def fill_missing(df, column, strategy='mean'):
    if strategy == 'mean':
        df[column] = df[column].fillna(df[column].mean())
    return df

def remove_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    df = df[(df[column] >= Q1 - 1.5 * IQR) & (df[column] <= Q3 + 1.5 * IQR)]
    return df

# Sample DataFrame
df = pd.DataFrame({'A': [1, 2, None, 100, 4], 'B': [5, None, 7, 8, 9]})

# Create pipeline
cleaned_df = (df.pipe(fill_missing, column='A', strategy='mean')
                .pipe(remove_outliers, column='A'))

print(cleaned_df)
```

**Why Use Pipelines?** Pipelines improve code readability and modularity, making it easier to apply multiple transformations sequentially.

---

### 5. Hands-On: Clean Attendance Dataset
**Task:** Clean a sample attendance dataset (`____.csv`) for analysis.

#### Dataset Description:
- Columns: `student_id`, `name`, `attendance_date`, `status` (Present/Absent), `score`.
- Issues: Missing values in `score`, outliers in `score`, incorrect data types, and unparsed dates.

#### Steps to Implement:
1. **Load the Dataset:** Use `pd.read_csv()` to load the dataset.
2. **Handle Missing Values:** Choose an imputation method (e.g., median for `score`) or drop rows with missing values based on your analysis.
3. **Detect and Handle Outliers:** Use IQR or Z-score to identify outliers in `score` and decide whether to remove or cap them.
4. **Convert Data Types:** Parse `attendance_date` to datetime, convert `status` to category, and ensure `student_id` and `score` are appropriate types (e.g., integer, float).
5. **Create a Pipeline:** Use `.pipe()` to chain cleaning steps for modularity.
6. **Inspect Results:** Use `.info()` and `.head()` to verify the cleaned dataset.

**Challenge:** Experiment with different imputation methods (e.g., mean vs. median) and outlier handling strategies (e.g., remove vs. cap). Justify your choices based on the dataset’s characteristics.

---

## Resources
- **Pandas Documentation:** [pandas.pydata.org](https://pandas.pydata.org/docs/) – Official guide for Pandas functions and methods.
- **Anaconda Installation Guide:** [docs.anaconda.com](https://docs.anaconda.com/anaconda/install/) – Instructions for setting up Anaconda.
- **Python pip Documentation:** [pip.pypa.io](https://pip.pypa.io/en/stable/) – Guide for installing Python packages with pip.
- **Jupyter Notebooks:** [jupyter.org](https://jupyter.org/) – Tutorials for using Jupyter for interactive coding.
- **Open-Source Datasets:** [Kaggle Datasets](https://www.kaggle.com/datasets) – Explore datasets for practice.
- **Scikit-learn Documentation:** [scikit-learn.org](https://scikit-learn.org/stable/) – Reference for advanced imputation methods like KNN.
- **Python Datetime Guide:** [docs.python.org/3/library/datetime.html](https://docs.python.org/3/library/datetime.html) – Details on handling dates and times.
- **RegEx Tutorial:** [https://docs.python.org/3/howto/regex.html](https://docs.python.org/3/howto/regex.html) - Details on how to compose Regular expressions in Python for data analysis 



Happy learning, and let’s dive into data science!
