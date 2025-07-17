# 📊 Interactive Charts Advanced Visualizations
**Theme:** Interactive, Hierarchical, and Multidimensional Charts with Plotly

---

## 🎯 Overview


This tutorial introduces charts that are difficult or impossible to create using traditional libraries, and showcases how Plotly enables seamless interaction and customization.

---

## 1️⃣ Sunburst Chart – 📌 Hierarchical Data in a Radial Layout

**Use Case:** Visualizing nested categories (e.g., Continent → Country)

```python
import plotly.express as px

df = px.data.gapminder().query("year == 2007")
fig = px.sunburst(df, path=['continent', 'country'], values='pop',
                  title="🌍 Population Breakdown by Continent and Country")
fig.show()
````

**Expected Output:**

* A circular interactive chart where segments expand outward based on hierarchy.
* Hovering reveals population and hierarchy information.
* Clicking on a segment zooms into that branch.

---

## 2️⃣ Treemap – 🧱 Space-Filling Proportion Visualization

**Use Case:** Comparing values across hierarchical categories.

```python
fig = px.treemap(df, path=['continent', 'country'], values='pop',
                 title="📦 Population Treemap by Country")
fig.show()
```

**Expected Output:**

* A color-coded treemap with rectangles sized by population.
* Hovering shows continent, country, and exact values.
* Useful for dashboards and comparisons across categories.

---

## 3️⃣ Animated Scatter Plot – 🕐 Trends Over Time

**Use Case:** Showing changes over time (GDP, population, etc.)

```python
fig = px.scatter(px.data.gapminder(), x="gdpPercap", y="lifeExp", animation_frame="year",
                 size="pop", color="continent", hover_name="country", log_x=True, size_max=60)
fig.show()
```

**Expected Output:**

* Animated timeline showing global development.
* Dynamic plot updates by year.
* Hover text and transitions enable storytelling over time.

---

## 4️⃣ 3D Surface Plot – 🔺 Visualizing Mathematical Functions

**Use Case:** Plotting surfaces or high-dimensional function outputs.

```python
import plotly.graph_objects as go
import numpy as np

x = np.linspace(-2, 2, 50)
y = np.linspace(-2, 2, 50)
x, y = np.meshgrid(x, y)
z = np.sin(x**2 + y**2)

fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])
fig.update_layout(title='🧠 3D Surface Plot of sin(x² + y²)')
fig.show()
```

**Expected Output:**

* Interactive 3D chart with rotation, zoom, and hover values.
* Useful for mathematical modeling, ML surfaces, or terrain maps.

---

## 5️⃣ Parallel Coordinates – 🧬 Multi-Dimensional Comparison

**Use Case:** Exploring relationships between multiple numeric features.

```python
fig = px.parallel_coordinates(df,
                              dimensions=["gdpPercap", "lifeExp", "pop"],
                              color="lifeExp",
                              color_continuous_scale=px.colors.diverging.Tealrose)
fig.update_layout(title='🔗 Parallel Coordinates: GDP, Life Expectancy, Population')
fig.show()
```

**Expected Output:**

* Multiple vertical axes with colored lines representing each country.
* Visualizes patterns across variables.
* Hover highlights and color gradients enhance interpretability.

---

## 6️⃣ Choropleth Map – 🗺️ Interactive Geographic Visualization

**Use Case:** Plotting world data on maps (e.g., GDP, population)

```python
fig = px.choropleth(df, locations="iso_alpha", color="lifeExp",
                    hover_name="country", animation_frame="year",
                    color_continuous_scale=px.colors.sequential.Plasma,
                    title="🗺️ Life Expectancy Over Time (Animated)")
fig.show()
```

**Expected Output:**

* A dynamic, animated world map.
* Hover text shows country-specific data.
* Year-wise transitions provide storytelling through geography.

---

## 7️⃣ Linked Brushing with Facets – 🔍 Interactions Across Charts

**Use Case:** Comparing subsets across dimensions with selection-based filtering.

```python
fig = px.scatter(df.query("year==2007"), x="gdpPercap", y="lifeExp",
                 color="continent", hover_name="country", facet_col="continent",
                 title="📊 GDP vs Life Expectancy per Continent (2007)")
fig.show()
```

**Expected Output:**

* Multiple scatter plots side-by-side by continent.
* Hover interactions persist across subplots.
* Faceting makes comparison intuitive.

---

## 🧠 Why These Charts Matter

| Feature                     | Matplotlib/Seaborn | Plotly                 |
| --------------------------- | ------------------ | ---------------------- |
| Interactivity (Hover, Zoom) | ❌                  | ✅ Built-in             |
| Hierarchical Charts         | ❌                  | ✅ Sunburst, Treemap    |
| Animated Visualizations     | ❌                  | ✅ Time slider + frames |
| 3D Graphs                   | ⚠️ Basic           | ✅ Highly interactive   |
| Geographic Mapping          | ⚠️ Complex         | ✅ One-liner support    |
| Linked Brushing             | ❌                  | ✅ Native               |
| Dashboards & Web App Use    | ❌                  | ✅ Dash integration     |

---

## 📚 References & Docs

* [📘 Plotly Express Documentation](https://plotly.com/python/plotly-express/)
* [🌍 Plotly Maps Gallery](https://plotly.com/python/maps/)
* [🔢 Plotly Graph Objects](https://plotly.com/python/graph-objects/)
* [📦 Sample Datasets in Plotly](https://plotly.com/python-api-reference/plotly.express.html#plotly-express)
* [📂 Dash Framework (for apps)](https://dash.plotly.com/)

---

## ✅ Key Takeaways

* Use **sunburst** and **treemap** for **hierarchical breakdowns**.
* Use **animations and sliders** to show **trends over time**.
* Use **3D surface plots** and **parallel coordinates** for **multidimensional modeling**.
* Use **choropleths** and **facet grids** for **spatial and segmented analysis**.

These visualizations are **essential for dashboards**, **interactive reports**, and **executive storytelling**.

---
