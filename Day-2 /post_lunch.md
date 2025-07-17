# 🎨 Day 2: Exploratory Visualization with Matplotlib & Seaborn  
**Duration:** 2 hours (Post-Lunch)  
**Theme:** Visualizing insights using foundational and statistical plotting techniques.

---

## 🧠 Learning Objectives

By the end of this session, you should be able to:

- Create and customize visualizations using Matplotlib.
- Leverage Seaborn for statistical plots and insights.
- Design subplots and facet grids to compare data across categories.
- Understand and apply good visualization practices.

---

## 1️⃣ Matplotlib Fundamentals

### ✅ Anatomy of a Plot

- **Figure**: Entire canvas.
- **Axes**: The plotting area (can be multiple per figure).
- **Axis**: X and Y axes within an Axes object.

### 🔧 Basic Plot Types

```python
import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 17, 18]

# Line plot
plt.plot(x, y, marker='o', linestyle='-', color='b')
plt.title('Line Plot Example')
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.grid(True)
plt.show()
````

### 🎨 Customizations

```python
plt.figure(figsize=(6,4))
plt.bar(x, y, color='green', alpha=0.7)
plt.title('Bar Chart')
plt.xlabel('Category')
plt.ylabel('Value')
plt.xticks(rotation=45)
plt.legend(['Sample Data'])
plt.tight_layout()
plt.show()
```

---

## 2️⃣ Seaborn for Statistical Graphics

Seaborn makes it easy to generate beautiful, high-level statistical visualizations.

### 📊 Boxplot, Violin Plot, Histogram

```python
import seaborn as sns
import pandas as pd

# Load sample data
tips = sns.load_dataset("tips")

# Boxplot
sns.boxplot(data=tips, x='day', y='total_bill')
plt.title("Boxplot of Total Bill by Day")
plt.show()

# Violin plot
sns.violinplot(data=tips, x='day', y='tip')
plt.title("Violin Plot of Tips by Day")
plt.show()

# Histogram with KDE
sns.histplot(data=tips, x='total_bill', bins=20, kde=True)
plt.title("Histogram of Total Bill")
plt.show()
```

---

### 🔥 Heatmaps & Correlation Matrices

```python
# Heatmap for correlations
corr = tips.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
```

---

## 3️⃣ Facets and Subplots

### 📐 FacetGrid with Seaborn

```python
g = sns.FacetGrid(tips, col="sex", row="time")
g.map_dataframe(sns.histplot, x="total_bill")
plt.show()
```

### 🔳 Subplots with Matplotlib

```python
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Histogram on left
axes[0].hist(tips['total_bill'], bins=20, color='skyblue')
axes[0].set_title('Total Bill Distribution')

# Scatter on right
axes[1].scatter(tips['total_bill'], tips['tip'], alpha=0.7)
axes[1].set_title('Tip vs. Total Bill')

plt.tight_layout()
plt.show()
```

---

## 4️⃣ Best Practices for Plotting

| Do                            | Avoid                                 |
| ----------------------------- | ------------------------------------- |
| Label axes and titles clearly | Overcrowding with too much data       |
| Use consistent color palettes | Misleading axes or truncated scales   |
| Add legends and annotations   | Unnecessary 3D effects or chart junk  |
| Use grid and layout properly  | Irrelevant elements (clipart, emojis) |

---

## 💻 Hands-On Exercises

### 📁 Dataset: Use your cleaned dataset from Day 1 (e.g., `sales.csv` or `attendance.csv`)

### ✅ Task 1 – Sales by Region Bar Chart

```python
# Group and plot
sales_by_region = sales.groupby('region')['revenue'].sum().reset_index()
sns.barplot(data=sales_by_region, x='region', y='revenue')
plt.title('Total Sales by Region')
plt.xticks(rotation=45)
plt.show()
```

---

### ✅ Task 2 – Price Distribution Histogram

```python
sns.histplot(data=sales, x='price', bins=30, kde=True)
plt.title("Price Distribution")
plt.xlabel("Price")
plt.ylabel("Count")
plt.show()
```

---

### ✅ Task 3 – Correlation Heatmap

```python
numeric_cols = sales.select_dtypes(include='number')
corr_matrix = numeric_cols.corr()
sns.heatmap(corr_matrix, annot=True, cmap="YlGnBu")
plt.title("Sales Data Correlation Matrix")
plt.show()
```

---

## 🔍 Challenge (Optional)

Use `FacetGrid` or `plt.subplots()` to create **multi-panel comparisons**, such as:

* Price distribution by category.
* Revenue trends by quarter or store type.
* Tips vs total bill comparison across days.

---

## 📚 References

* [Matplotlib Docs](https://matplotlib.org/stable/)
* [Seaborn Docs](https://seaborn.pydata.org/)
* [DataViz Best Practices](https://www.data-to-viz.com/)
* [Color Palettes Reference](https://seaborn.pydata.org/tutorial/color_palettes.html)

---

Happy plotting! 🎉
