# 📈 Day 2: Acquisition & Exploratory Visualization  
**Theme:** Getting data from the web and creating initial visual insights  
**Duration:** 2 hours (Pre-Lunch)

---
**LIVE UPDATE:** Day 2 [Quiz Link](https://docs.google.com/forms/d/e/1FAIpQLSfwQuBstq1f5sWCWaB2CNX71ccN3y7P_CHi_98r2mVZYQrLUQ/viewform?usp=sharing&ouid=100366893311897454689)
---

## 🔹 Overview

In this session, we explore how to collect data from the web using scraping techniques. Many real-world datasets are not neatly packaged in CSVs or databases — they exist on websites. You'll learn how to extract that data using **BeautifulSoup** for static content and **Selenium** for dynamic JavaScript-rendered pages.

---

## 🧠 Learning Objectives

By the end of this session, you should be able to:

- Understand the structure of web pages (DOM, HTML, CSS).
- Extract data from static websites using **BeautifulSoup**.
- Extract data from dynamic websites using **Selenium**.
- Load scraped data into Pandas for analysis.

---

## 1️⃣ HTML Structure & Selectors

### ✅ What is DOM?
- DOM (Document Object Model) is the tree-like structure of HTML elements.
- Every webpage is composed of nested tags like `<html>`, `<head>`, `<body>`, etc.

### 🛠 Inspecting Elements
- Right-click → Inspect Element (in Chrome/Firefox)
- Use **browser dev tools** to identify class names, tags, IDs.

### 🎯 Selectors: CSS vs. XPath

When you're scraping websites using **BeautifulSoup** or **Selenium**, you need to tell your script exactly where in the HTML document to look. That’s where **selectors** come in.

#### 🧩 What Are Selectors?

Selectors are instructions that help extract specific HTML elements based on tags, attributes, or hierarchy. The two most commonly used types are **CSS Selectors** and **XPath**.

---

#### 📌 CSS Selectors

CSS selectors are widely used in front-end web development and are very intuitive for selecting elements based on:

* **Tag names**: `h1`, `p`, `div`, etc.
* **Class names**: `.classname`
* **ID attributes**: `#elementId`
* **Attribute values**: `input[type='text']`

##### ✅ Common CSS Selector Examples:

| Selector             | Meaning                                       |
| -------------------- | --------------------------------------------- |
| `div`                | Selects all `<div>` elements                  |
| `.price`             | Selects all elements with class "price"       |
| `#main-content`      | Selects the element with ID "main-content"    |
| `ul > li`            | Selects direct `<li>` children of `<ul>`      |
| `a[href*="product"]` | Selects `<a>` tags with "product" in the link |

#### 🛠️ Usage in BeautifulSoup:

```python
soup.select("div.price")      # using class selector
soup.select("ul > li")        # direct child elements
```

---

#### 📌 XPath Selectors

XPath (XML Path Language) is more powerful and expressive, especially for **deeply nested**, **dynamically generated**, or **attribute-heavy** elements. It's based on path expressions.

##### ✅ Common XPath Selector Examples:

| XPath Expression                   | Meaning                                               |
| ---------------------------------- | ----------------------------------------------------- |
| `//div`                            | Select all `<div>` tags anywhere                      |
| `//div[@class="price"]`            | Select all `<div>` tags with class "price"            |
| `//a[contains(@href, "product")]`  | Select `<a>` tags where the `href` contains "product" |
| `//table[@id="stats"]/tr[2]/td[1]` | Target specific table cell by position                |

#### 🛠️ Usage in Selenium:

```python
driver.find_element(By.XPATH, '//div[@class="price"]')
```

---

### 🧠 Which Should You Use?

| Use Case                              | Recommended Selector |
| ------------------------------------- | -------------------- |
| Simple tag or class identification    | **CSS**              |
| You already use CSS in dev tools      | **CSS**              |
| Deeply nested elements                | **XPath**            |
| Element based on text or conditions   | **XPath**            |
| Selecting by attribute with wildcards | **XPath**            |

---

### 🎯 Tips for Precision

* ✅ Use **Chrome DevTools** → Right-click an element → `Inspect` → Right-click → "Copy > Copy selector" or "Copy XPath".
* ✅ Paste into your script as your search target.
* ⚠ Be cautious with long or dynamic XPath chains like `//*[@id="root"]/div/div[2]/table/...` — they may break on small site changes.

---

### 📌 Practice Exercise

Open this demo site: [https://books.toscrape.com](https://books.toscrape.com)

Try inspecting the book titles:

1. Use **CSS selector**:

   ```python
   soup.select("article.product_pod h3 a")
   ```

2. Use **XPath** (in Selenium):

   ```python
   driver.find_element(By.XPATH, '//article[@class="product_pod"]//h3/a')
   ```


---

## 2️⃣ Scraping Static Pages with BeautifulSoup

### 🔧 Required Libraries
```bash
pip install requests beautifulsoup4 pandas
````

### ✏️ Step-by-Step Example: Scraping Book Titles

```python
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Request the web page
url = "http://books.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Step 2: Extract product details
books = soup.select('article.product_pod')
data = []
for book in books:
    title = book.h3.a['title']
    price = book.select_one('.price_color').text
    rating = book.p['class'][1]
    data.append([title, price, rating])

# Step 3: Convert to DataFrame
df = pd.DataFrame(data, columns=['Title', 'Price', 'Rating'])
print(df.head())
```

### 📌 Techniques:

* `select()`: for CSS selectors
* `find() / find_all()`: for tag-specific searching
* Use `.text`, `.attrs`, and indexing for attributes

---

## 3️⃣ Extracting Tables and Lists into Pandas

### 🔗 HTML Table Example

```python
url = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"
tables = pd.read_html(url)
print(f"Number of tables found: {len(tables)}")

# View first table
gdp_df = tables[2]
print(gdp_df.head())
```

This works well for **structured tables** in clean HTML.

---

## 4️⃣ Scraping Dynamic Pages with Selenium

When websites load content using JavaScript (e.g., YouTube comments, Amazon reviews), `requests` and `BeautifulSoup` won’t see it. **Selenium** mimics user interaction by running a browser.

### 🧰 Installation

```bash
pip install selenium
```

Also install **ChromeDriver** matching your browser version:
[https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)

---

### ✏️ Example: Scraping YouTube Comments

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

# Set up headless browser
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

# Load page
driver.get("https://www.youtube.com/watch?v=VIDEO_ID")
time.sleep(5)  # wait for comments to load

# Scroll to load dynamic comments
for _ in range(3):
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(3)

# Extract comment elements
comments = driver.find_elements(By.CSS_SELECTOR, '#content-text')
comment_texts = [comment.text for comment in comments]

# Save to DataFrame
df_comments = pd.DataFrame(comment_texts, columns=["Comment"])
print(df_comments.head())

driver.quit()
```

> ✅ Replace `"VIDEO_ID"` with actual ID like `"dQw4w9WgXcQ"`

---

## 5️⃣ Hands-On Lab

Choose ONE of the following projects:

### 🧪 Project A – Book Store Scraping with BeautifulSoup

* URL: [http://books.toscrape.com](http://books.toscrape.com)
* Scrape:

  * Book Title
  * Price
  * Star Rating
* Store in a DataFrame and save as `books.csv`

### 🧪 Project B – YouTube Comment Scraper using Selenium

* Input: A YouTube video URL
* Scrape:

  * Top 20 Comments
  * Clean whitespace
  * Save to `youtube_comments.csv`

### ✅ Bonus Ideas:

* Scrape top 10 IMDb movies from [https://www.imdb.com/chart/top](https://www.imdb.com/chart/top)
* Extract job titles and companies from [https://remoteok.com](https://remoteok.com)

---

## 🔚 Summary of Key Commands

| Tool            | Command / Function       | Purpose                       |
| --------------- | ------------------------ | ----------------------------- |
| `requests`      | `requests.get()`         | Download static web content   |
| `BeautifulSoup` | `soup.find_all()`        | Parse HTML with tag/attribute |
| `Selenium`      | `driver.find_elements()` | Locate dynamic page elements  |
| `pandas`        | `pd.read_html()`         | Directly import HTML tables   |

---

## 📚 Resources

* [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [Selenium Docs](https://www.selenium.dev/documentation/)
* [ChromeDriver Setup](https://chromedriver.chromium.org/)
* [HTML/CSS Selectors Guide](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors)
* [XPath Tutorial](https://www.w3schools.com/xml/xpath_intro.asp)
* [YouTube Video Comment Scraper (GitHub)](https://github.com/egbertbouman/youtube-comment-downloader)

---

Happy scraping! 🚀
