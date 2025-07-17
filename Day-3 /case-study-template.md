# 📁 Case Study: Time Series Analysis for Activity Detection using Smartwatch Data

## 🧠 Problem Statement

**Objective:**  
Develop a time-series based system to **detect human physical activities** (walking, running, sitting, etc.) using sensor data (accelerometer and gyroscope) collected from a smartwatch.

Smartwatch sensors generate multivariate time-series data at high frequency. By analyzing this temporal data, we aim to identify meaningful activity patterns and transitions using statistical and ML tools.

---

## 📦 Dataset Description

We use a public dataset from [UCI HAR Dataset](https://archive.ics.uci.edu/ml/datasets/human+activity+recognition+using+smartphones) containing the following:

- **Sampling rate:** 50Hz  
- **Features:**  
  - Accelerometer (X, Y, Z)
  - Gyroscope (X, Y, Z)
- **Target labels (Activities):**  
  - Walking, Walking Upstairs, Walking Downstairs  
  - Sitting, Standing, Laying

### Sample Columns:

| Time | acc_x | acc_y | acc_z | gyro_x | gyro_y | gyro_z | activity |
|------|-------|-------|-------|--------|--------|--------|----------|
| t₀   | 0.02  | -0.01 | 0.98  | 0.003  | -0.002 | 0.005  | Walking  |

---

## 🔍 Exploratory Data Analysis (EDA)

### ✅ Step 1: Visualize Raw Sensor Time Series

```python
import matplotlib.pyplot as plt

df[df['activity'] == 'Walking'][['acc_x', 'acc_y', 'acc_z']].plot(figsize=(12, 4), title="Walking - Accelerometer Signals")
plt.show()
````

> 💡 Insight: Each activity shows a distinct pattern in its axis-aligned accelerometer data.

---

### ✅ Step 2: Aggregate with Rolling Statistics

```python
df['acc_mag'] = (df['acc_x']**2 + df['acc_y']**2 + df['acc_z']**2)**0.5
df['acc_mag_roll_mean'] = df['acc_mag'].rolling(window=50).mean()

df[['acc_mag', 'acc_mag_roll_mean']].plot(figsize=(12, 4), title="Rolling Magnitude of Acceleration")
plt.show()
```

> 💡 Insight: Rolling mean smooths out noise and helps in detecting transitions.

---

### ✅ Step 3: Resample for Lower Frequency

```python
df_resampled = df.resample('200ms', on='timestamp').mean().dropna()
```

> 💡 Insight: Resampling reduces computational load and preserves motion patterns.

---

## 🔁 Feature Engineering for Classification

| Feature                          | Description                                 |
| -------------------------------- | ------------------------------------------- |
| Mean, Std, Min, Max (per window) | Over 2-3 second windows (e.g., 100 samples) |
| Signal magnitude area (SMA)      | Sum of absolute accelerations               |
| Energy                           | Sum of squared values                       |
| FFT Coefficients                 | Dominant frequency components               |

```python
import numpy as np

window_size = 100
features = []
labels = []

for i in range(0, len(df) - window_size, window_size):
    window = df.iloc[i:i+window_size]
    acc_x = window['acc_x'].values
    features.append([np.mean(acc_x), np.std(acc_x), np.max(acc_x), np.min(acc_x)])
    labels.append(window['activity'].mode()[0])
```

---

## 📊 Activity Detection with Machine Learning

Train a classifier to recognize patterns from extracted features:

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

clf = RandomForestClassifier(n_estimators=100)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))
```

> 🎯 Expected Accuracy: \~92–95%
> 💡 Insight: Random forest performs well on temporal sensor windows.

---

## 📈 Time-Series Insights

* **Walking:** Periodic and high magnitude in `acc_z`
* **Sitting:** Very low variance in all axes
* **Transitions (e.g., standing → sitting):** Identifiable by drops in magnitude and change in slope
* **Rolling energy or variance** can indicate dynamic vs static states.

---

## 🔮 Optional: Real-Time Forecasting for Trend Prediction

Using **rolling window prediction** or **simple RNN/ARIMA**, we can forecast upcoming activity transitions (e.g., "user is about to sit down").

```python
from statsmodels.tsa.ar_model import AutoReg

model = AutoReg(df['acc_mag_roll_mean'].dropna(), lags=10)
model_fit = model.fit()
forecast = model_fit.predict(start=len(df), end=len(df)+20)
```

---

## 🧠 Summary

| Task                 | Method                                  |
| -------------------- | --------------------------------------- |
| Sensor preprocessing | Rolling mean, resampling                |
| Pattern recognition  | Feature extraction (mean, std, etc.)    |
| Classification       | Random Forest or SVM                    |
| Time-series analysis | Trend detection, smoothing              |
| Forecasting          | AutoReg, ARIMA, or deep learning models |

---

## 📚 References

* [UCI HAR Dataset](https://archive.ics.uci.edu/ml/datasets/human+activity+recognition+using+smartphones)
* [Feature Engineering for Sensor Data](https://towardsdatascience.com/feature-engineering-on-time-series-ae61061558b4)
* [Rolling & Window Functions in Pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/window.html)
* [Time-Series Forecasting Resources](https://machinelearningmastery.com/time-series-forecasting/)

---

🕒 *From acceleration to activity, time-series analysis makes wearables truly smart.*
