# Hands-on Data Science Workshop - IIT Bhilai

Welcome! This repository contains all the necessary resources, notebooks, datasets, and practice materials for students attending the **Data Science & Visualization Workshop** at IIT Bhilai.

Our goal is to move beyond theory and dive into practical, real-world data challenges. Throughout this workshop, you will:

- 🚀 **Build practical data analytics and visualization skills** from the ground up.
- 📊 **Work with real, messy datasets** to master data wrangling.
- 🧠 **Sharpen your problem-solving abilities** through hands-on exercises.
- 🗣️ **Develop critical thinking, mindfulness, and data story-telling capabilities.**

--- Live Updates ---------------

- July 12: Please fill out this pre-workshop survey form: https://forms.gle/p3WZkwD4Wh9nureU7
- July 12: Loaded practice files (leaves, survey) in Day 1 folder for data cleaning, exploration, model building



## 🗓️ Workshop Schedule

### ☀️ Day 1: Foundations—Loading, Cleaning & Preprocessing

**Theme:** Mastering the fundamentals of data handling with Pandas.

#### Pre-Lunch
*We kick off with a brief welcome and environment setup—verifying that Anaconda, Pandas, and Jupyter are working.*
- **Introduction to Pandas Data Structures**
  - `Series` vs. `DataFrame`: When to use each.
  - Indexing, slicing (`.loc`, `.iloc`), and selecting subsets of data.
- **Reading and Writing Data**
  - Loading data from CSV, Excel, JSON, and SQL sources.
  - Common gotchas: encoding issues, delimiters, and large-file chunking.
  - Exporting cleaned or transformed data back to disk.
- **Performance Tips**
  - Using `dtype` specifications to speed up reading.
  - When to use `read_csv` parameters like `usecols`, `chunksize`, and `iterator`.

**💻 Hands-On:** Participants will load an open-source CSV dataset, inspect its `shape` and `dtypes`, and practice basic data selection.

#### Post-Lunch
*We move into data cleaning and preprocessing—the essential “data wrangling” phase that underpins all analysis.*
- **Handling Missing Data**
  - Strategies: Dropping (`dropna`) vs. imputing (mean/median/mode).
  - Trade-offs: When to drop rows vs. columns (sample size vs. bias).
- **Outlier Detection and Treatment**
  - Identifying outliers using IQR and Z-scores.
  - Capping/extending or transforming (e.g., log) to tame extreme values.
- **Type Conversions & Date Handling**
  - Converting strings to `categorical` or `datetime` types for efficiency.
  - Parsing mixed-format date columns with `to_datetime` and extracting attributes (`.dt.year`, `.dt.month`).
- **Pipelines and Method Chaining**
  - Building readable, step-by-step transformations using `.pipe()` and chained methods.

**💻 Hands-On:** Working on a messy dataset (e.g., attendance sheet for DSL250), each group will clean missing values, normalize text fields (lower-casing, trimming), convert date strings, and produce a tidy DataFrame ready for analysis.

### 📈 Day 2: Acquisition & Exploratory Visualization

**Theme:** Getting data from the web and creating initial visual insights.

#### Pre-Lunch
*We delve into web data acquisition—learning how to scrape static and dynamic pages.*
- **HTML Structure & Selectors**
  - Understanding the DOM; using browser dev-tools to inspect elements.
  - CSS selectors vs. XPath: when each excels.
- **BeautifulSoup for Static Pages**
  - Fetching HTML with `requests`; parsing tags, attributes, and text.
  - Extracting tables, lists, and links directly into Pandas DataFrames.
- **Selenium for JavaScript-Heavy Sites**
  - Automating a headless browser to render pages and interact with elements.
  - Dealing with dynamic content, login forms, and infinite scroll.

**💻 Hands-On:** Scrape product information (e.g., name, price, rating) from an e-commerce page using BeautifulSoup, or extract YouTube comments using Selenium.

#### Post-Lunch
*Next, we explore core plotting techniques in Matplotlib and higher-level convenience in Seaborn.*
- **Matplotlib Fundamentals**
  - The anatomy of a plot: `Figure`, `Axes`, and basic plot types (line, bar, scatter).
  - Customizing labels, titles, legends, and annotations.
- **Seaborn for Statistical Graphics**
  - Quick creation of boxplots, violin plots, heatmaps, and pairplots.
  - Using color palettes and themes to enhance readability.
- **Facets & Subplots**
  - Organizing multiple plots in a grid to compare categories or time periods.
- **Best Practices**
  - Choosing the right plot for your question; avoiding “chart junk.”

**💻 Hands-On:** Using yesterday’s cleaned dataset, create sales-by-region bar charts, price-distribution histograms, and correlation heatmaps showing relationships between variables.

### 📊 Day 3: Interactive Charts & Time Series Analysis

**Theme:** Bringing data to life with interactivity and analyzing temporal patterns.

#### Pre-Lunch
*We move from static plots to interactive visualizations with Plotly.*
- **Interactivity Features**
  - Tooltips, zooming, panning, and linked brushing across subplots.
  - Embedding callbacks for simple dashboard-like behavior.

**💻 Hands-On:** Convert a Matplotlib/Seaborn plot into an interactive Plotly chart with hover-text. Add a dropdown to filter by category or year. Explore more advanced visuals like t-SNE or sunburst charts.

#### Post-Lunch
*Introduction to time-series analytics—resampling, rolling statistics, and basic forecasting.*
- **Datetime Indexing & Resampling**
  - Converting columns to a `DatetimeIndex`; upsampling vs. downsampling.
  - Aggregating (`mean`, `sum`, `count`) over time periods (daily, monthly, quarterly).
- **Rolling and Window Functions**
  - Computing moving averages, rolling standard deviations, and exponential-weighted stats.
- **Decomposition & Stationarity**
  - Splitting a series into trend, seasonal, and residual components using `statsmodels`.
  - Testing for stationarity (ADF test) and applying differencing.

**💻 Hands-On:** Analyze a historical stock-price CSV. Resample to weekly frequency, plot 20-day and 50-day moving averages, decompose the series, and fit a simple ARIMA model to forecast the next month.

### 🌐 Day 4: Network Analysis & BI Dashboards

**Theme:** Exploring relationships in data and communicating insights through dashboards.

#### Pre-Lunch
*We explore graph data with NetworkX and visualize it in Gephi.*
- **Graph Theory Basics**
  - Nodes, edges, directed vs. undirected, and weighted graphs.
  - Common metrics: degree centrality, betweenness, and clustering coefficient.
- **NetworkX Workflow**
  - Building graphs from edge lists or adjacency matrices.
  - Computing centrality measures, shortest paths, and community detection.
- **Gephi for Visual Analytics**
  - Exporting `.gexf` or CSV graph files from NetworkX.
  - Applying layout algorithms (e.g., ForceAtlas2, Yifan Hu) and styling nodes/edges by metrics.

**💻 Hands-On:** Create a social network graph (e.g., from a friend network dataset) in NetworkX, calculate key centralities, export to Gephi, and produce a visually compelling network diagram.

#### Post-Lunch
*We turn to dashboarding in a Business Intelligence (BI) tool like Power BI or Tableau.*
- **Connecting Data Sources**
  - Importing data from CSV, Excel, SQL Server, or web APIs into Power BI Desktop.
  - Data modeling: defining relationships, creating calculated columns, and DAX measures.
- **Building Reports**
  - Using visuals: bar/line charts, maps, KPI cards, slicers, and filters.
  - Designing interactive dashboards that let end-users drill down and explore.
- **Publishing & Sharing**
  - Deploying to Power BI Service, setting up scheduled refresh, and managing access.

**💻 Hands-On:** Connect to a sample sales database, build a multi-page report in Power BI showing regional performance, top products, and sales trends over time.

### 🤖 Day 5: Machine Learning & Streaming Data

**Theme:** Building predictive models and understanding real-time data processing.

#### Pre-Lunch
*An overview of supervised and unsupervised modeling with scikit-learn.*
- **Regression Methods**
  - Linear Regression vs. tree-based regressors (e.g., RandomForestRegressor).
  - Feature scaling and creating polynomial features.
- **Classification Algorithms**
  - Logistic Regression, Support Vector Machines (SVMs), Random Forests, and Gradient Boosting.
  - Handling class imbalance with techniques like SMOTE or class weights.
- **Clustering Techniques**
  - K-Means vs. density-based clustering (DBSCAN).
  - Selecting the optimal number of clusters (Elbow method, Silhouette score).

**💻 Hands-On:** Train a regression model on housing-price data (evaluating with R²/MSE), build a classifier for a leaves dataset (evaluating with precision/recall), and cluster customer profiles to identify distinct segments.

#### Post-Lunch
*We conclude with model evaluation and an introduction to streaming data concepts.*
- **Evaluation Metrics Deep Dive**
  - Regression: MAE, MSE, RMSE, R² — choosing the right metric for the business context.
  - Classification: Confusion Matrix, Accuracy, Precision, Recall, F1-score, and ROC-AUC curve.
  - Clustering: Silhouette score.
- **Real-Time vs. Batch Processing**
  - Understanding the trade-offs in latency, throughput, and statefulness.
- **Streaming Analytics Basics**
  - Introduction to the streaming paradigm.
  - Windowed computations and aggregations over event streams.

**💻 Hands-On:** Evaluate the models built earlier on a held-out test set, interpret the results, and discuss how a streaming version of the problem might work.

### 🏆 Day 6: Capstone Breakout Sessions

**Theme:** Apply your new skills to a domain-specific project of your choice.

On the final day, participants will form groups and choose a project track to work on. Instructors will provide guidance and support.

- **Track 1: Natural Language Processing (NLP)**
  - Project: Analyze customer reviews for sentiment or perform topic modeling on a corpus of news articles.
- **Track 2: Computer Vision (CV)**
  - Project: Build an image classifier to identify different types of objects or use object detection on a sample video.
- **Track 3: Generative AI (Gen AI)**
  - Project: Generate creative content such as text, images, or code using pre-trained models like GPT or Stable Diffusion.
---


