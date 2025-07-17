# 🌐 Day 4: Network Analysis & BI Dashboards

**Theme:** Exploring relationships in data and communicating insights through dashboards.

Welcome to Day 4! Today, we'll bridge the gap between complex data relationships and clear, actionable insights. In the morning, we'll map out networks using Python. In the afternoon, we'll build professional-grade, interactive dashboards.

---

## ☀️ Pre-Lunch: Network Analysis with NetworkX & Gephi

---
**LIVE UPDATES**: [LINK](https://forms.gle/4BozfCNokqeMzXUb7)
---

We'll start by exploring graph data, a powerful way to model and analyze connections—from social networks to financial transactions. We'll use the Python library **NetworkX** for computation and **Gephi** for stunning, interactive visualizations.

### 📈 Graph Theory Basics
Graphs are mathematical structures used to model relationships between objects. Understanding the basics is key to unlocking their power.
* **Nodes & Edges**: Nodes are the individual entities (e.g., people, airports), and edges are the connections between them (e.g., friendships, flight routes).
* **Directed vs. Undirected**: A directed edge has a one-way relationship (e.g., a Twitter follow), while an undirected edge is mutual (e.g., a Facebook friendship).
* **Weighted Graphs**: Edges can have a weight to represent the strength or cost of a connection (e.g., number of messages exchanged, distance between cities).
* **Common Metrics**:
    * **Degree Centrality**: Measures the number of connections a node has. A high degree centrality means the node is a major hub.
    * **Betweenness Centrality**: Identifies nodes that act as bridges between different parts of the network. Removing these nodes can fracture the network.
    * **Clustering Coefficient**: Tells us how likely a node's neighbors are to be connected to each other. It helps find tightly-knit communities.

### 🐍 NetworkX Workflow
**NetworkX** is the standard Python library for graph analysis. It allows you to create, manipulate, and study the structure and dynamics of complex networks.
* **Building Graphs**: You can easily create graph objects from various data formats, like pandas DataFrames (`nx.from_pandas_edgelist`) or adjacency matrices.
* **Computing Metrics**: NetworkX has built-in functions for all major graph metrics, such as `nx.degree_centrality()`, `nx.betweenness_centrality()`, and community detection algorithms.
* **Exporting**: Once your analysis is done, you can export the graph data into common formats like `.gexf` for use in visualization tools.

### 🎨 Gephi for Visual Analytics
**Gephi** is like Photoshop for graphs. It's an open-source tool for exploring and presenting networks. It helps turn complex network data into a story you can see.
* **Importing**: Easily import graph files like `.gexf` or CSV that you've exported from NetworkX.
* **Layout Algorithms**: These algorithms organize the nodes to reveal underlying structures. **ForceAtlas2** is excellent for showing clusters, while **Yifan Hu** is a fast, general-purpose choice.
* **Styling**: Customize your visualization by mapping data metrics to visual properties. For example, you can set node size based on its degree centrality or node color based on its community membership.

### 💻 Hands-On: Analyzing a Social Network
**Goal**: Create a compelling network diagram of a character co-occurrence network from Victor Hugo's *Les Misérables*.

**Dataset**:
* We will use the classic **Les Misérables Character Co-occurrence dataset**. You can find the edge list data [here](https://raw.githubusercontent.com/gephi/gephi/master/modules/Desktop/src/test/resources/org/gephi/desktop/importer/lesmiserables.csv) (CSV file).

**Steps**:
1.  **Load Data**: Use `pandas` to load the CSV file into a DataFrame.
2.  **Build Graph**: Use `NetworkX` to create a graph from the pandas DataFrame.
3.  **Calculate Metrics**: Compute the degree centrality for all characters.
4.  **Detect Communities**: Use the Louvain community detection algorithm to find character groups.
5.  **Export**: Save your graph, complete with its new metrics, as a `.gexf` file.
6.  **Visualize**: Import the `.gexf` file into Gephi. Use the **ForceAtlas2** layout algorithm, size the nodes by their **degree centrality**, and color them based on their **community**. Can you spot the main protagonist?

---

## 🌙 Post-Lunch: Business Intelligence (BI) Dashboards with Power BI

Next, we'll switch gears to visual storytelling with a BI tool like **Microsoft Power BI**. The focus is on converting raw data into interactive dashboards that empower users to find their own insights.

### 🔗 Connecting Data Sources
A dashboard is only as good as its data. Power BI can connect to hundreds of sources.
* **Importing Data**: We'll practice importing data from common formats like CSV and Excel. Power BI can also connect directly to databases (SQL Server, PostgreSQL) and web APIs.
* **Data Modeling & Transformation**: Inside the **Power Query Editor**, you can clean, shape, and transform your data. This is where you define relationships between tables (e.g., a star schema), create calculated columns, and write powerful **DAX (Data Analysis Expressions)** measures to define your key metrics.

### 📊 Building Reports
This is the creative part where you design the user experience.
* **Choosing Visuals**: We'll use a mix of visuals for different purposes:
    * **Bar/Line Charts**: For comparing categories and showing trends over time.
    * **Maps**: For visualizing geographical data.
    * **KPI Cards**: To highlight the most important top-line numbers.
    * **Slicers & Filters**: To give users control over what they see.
* **Designing for Interaction**: A great dashboard is interactive. We'll ensure our visuals cross-filter each other, allowing users to click on one element (like a country on a map) and see all other visuals update instantly.

### ☁️ Publishing & Sharing
Your analysis has no impact if it isn't shared.
* **Power BI Service**: We'll publish our local Power BI Desktop file (`.pbix`) to the cloud-based Power BI Service.
* **Scheduled Refresh**: To keep data current, you can set up a scheduled refresh that automatically pulls the latest data from your sources.
* **Sharing & Access**: Learn to share reports with colleagues, publish them as an "App" for wider consumption, and manage access permissions.

### 💻 Hands-On: Building an Interactive Sales Dashboard
**Goal**: Build a multi-page sales report in Power BI that provides a comprehensive overview of business performance.

**Dataset**:
* We'll use Microsoft's official **Sample Financial Dataset**. You can download the Excel file directly from [here](https://go.microsoft.com/fwlink/?LinkID=521962).

**Steps**:
1.  **Connect & Model**: Open Power BI Desktop, get data from the downloaded Excel file, and explore the Power Query Editor for any necessary cleanup.
2.  **Build a 'Summary' Page**:
    * Create **KPI cards** for Total Sales, Total Profit, and Total Units Sold.
    * Add **Slicers** for `Date` and `Country`.
3.  **Create a 'Product Analysis' Page**:
    * Add a **bar chart** showing `Sales` by `Product`.
    * Add a **donut chart** showing `Profit` by `Product Category`.
4.  **Design a 'Regional Performance' Page**:
    * Use the **Map** visual to display `Sales` by `Country`.
    * Add a **table** or **matrix** for a detailed breakdown of metrics by region.
5.  **Publish**: Make sure all visuals are interactive, then publish your report to the Power BI Service.

---

## 📚 Resources & Links

### Network Analysis
* **NetworkX**:
    * [Official Documentation](https://networkx.org/documentation/stable/)
    * [Tutorial](https://networkx.org/documentation/stable/tutorial.html)
* **Gephi**:
    * [Download Gephi](https://gephi.org/)
    * [Gephi Quick Start Tutorial (Video)](https://www.youtube.com/watch?v=20SE4_34-3c)
* **Graph Theory**:
    * [Intro to Graph Theory by FreeCodeCamp](https://www.freecodecamp.org/news/i-dont-understand-graph-theory-1c96572a1a28/)
* **Datasets**:
    * [Stanford Large Network Dataset Collection (SNAP)](http://snap.stanford.edu/data/)

### Business Intelligence
* **Power BI**:
    * [Download Power BI Desktop](https://powerbi.microsoft.com/en-us/desktop/)
    * [Microsoft Learn for Power BI](https://learn.microsoft.com/en-us/power-bi/) (Excellent structured learning paths)
* **DAX (Data Analysis Expressions)**:
    * [DAX Basics in Power BI Desktop](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-dax-basics)
    * [DAX.guide - A comprehensive DAX reference](https://dax.guide/)
* **Alternative Tool - Tableau**:
    * [Download Tableau Public](https://www.tableau.com/products/public/download) (Free version)
```
