# 📊 Hands-On: Exploratory Visualization with Social Media Addiction Dataset

**Dataset:** [Students Social Media Addiction](https://www.kaggle.com/datasets/adilshamim8/social-media-addiction-vs-relationships/data)  
**Objective:** Understand relationships between screen time, mental health, academic performance, and addiction patterns through data visualization.

---

## 🔍 Dataset Overview

This dataset contains responses from 705 students with the following attributes:

| Column                       | Description                                               |
|-----------------------------|-----------------------------------------------------------|
| `Age`                       | Age of the student                                        |
| `Gender`                    | Gender of the student                                     |
| `Academic_Level`            | Undergraduate, Graduate, Postgraduate                    |
| `Country`                   | Country of residence                                     |
| `Avg_Daily_Usage_Hours`     | Average daily hours spent on social media                |
| `Most_Used_Platform`        | Platform used most often (e.g., Instagram, WhatsApp)     |
| `Affects_Academic_Performance` | Whether social media affects their academics (Yes/No) |
| `Sleep_Hours_Per_Night`     | Average sleep hours per night                            |
| `Mental_Health_Score`       | Self-rated score from 1–10                               |
| `Relationship_Status`       | Single, In a Relationship, It's Complicated              |
| `Conflicts_Over_Social_Media` | Number of conflicts caused by social media usage      |
| `Addicted_Score`            | Addiction score (1–10 scale)                             |

---

## 📈 Visual Goals

We aim to:

- Visualize usage and addiction trends across age and gender.
- Understand the impact of usage on academic and mental health.
- Identify platform-specific behavioral patterns.
- Compare average sleep vs. addiction levels.

---

## 📊 Task 1: Average Daily Usage by Academic Level

```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.barplot(data=df, x='Academic_Level', y='Avg_Daily_Usage_Hours', ci=None)
plt.title('Average Daily Usage by Academic Level')
plt.ylabel('Hours per Day')
plt.xticks(rotation=45)
plt.show()
````

---

## 🧠 Task 2: Mental Health vs. Daily Usage (by Gender)

```python
sns.scatterplot(data=df, x='Avg_Daily_Usage_Hours', y='Mental_Health_Score', hue='Gender')
plt.title('Mental Health vs Daily Usage by Gender')
plt.xlabel('Daily Usage (Hours)')
plt.ylabel('Mental Health Score (1-10)')
plt.show()
```

---

## 💡 Task 3: Correlation Heatmap

```python
import pandas as pd

numeric_cols = df.select_dtypes(include='number')
corr = numeric_cols.corr()

sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap: Addiction, Mental Health & Usage')
plt.show()
```

---

## 🔄 Task 4: Sleep Hours by Addicted Score Category

```python
# Bin addiction scores
df['Addiction_Level'] = pd.cut(df['Addicted_Score'], bins=[0, 4, 7, 10], labels=['Low', 'Medium', 'High'])

sns.boxplot(data=df, x='Addiction_Level', y='Sleep_Hours_Per_Night')
plt.title('Sleep Hours by Addiction Level')
plt.ylabel('Sleep Hours')
plt.xlabel('Addiction Category')
plt.show()
```

---

## 🧪 Task 5: Usage Across Platforms

```python
platform_avg = df.groupby('Most_Used_Platform')['Avg_Daily_Usage_Hours'].mean().sort_values()

platform_avg.plot(kind='barh', figsize=(8, 6), color='skyblue')
plt.title('Average Usage Hours by Social Media Platform')
plt.xlabel('Average Hours')
plt.show()
```

---

## 📌 Summary Visual: Pairplot of Key Variables

```python
sns.pairplot(df[['Avg_Daily_Usage_Hours', 'Sleep_Hours_Per_Night', 'Mental_Health_Score', 'Addicted_Score']])
plt.suptitle("Pairplot: Addiction, Sleep, Mental Health, and Usage", y=1.02)
plt.show()
```

---

## 🧠 Analysis Questions (For Reflection)

* Which platform is linked with the highest usage?
* Do high addicted scores align with low sleep or mental health?
* Are students with more conflicts also reporting lower academic performance?

---

## 📚 Additional Resources

* [Seaborn Docs](https://seaborn.pydata.org/)
* [Matplotlib Docs](https://matplotlib.org/stable/)
* [Kaggle Dataset Hub](https://www.kaggle.com/datasets)

---

👨‍💻 *Use this notebook to explore causality and relationships in social media addiction and its effect on well-being. Submit your insights along with the final notebook link via the workshop form.*

Happy Analyzing! 🧠📊

