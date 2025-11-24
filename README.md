# Netflix User Behavior Analytics Dashboard
*An Academic Implementation of Manual Data Processing, Analytics, and Visualization With Custom Pandas*

---

## 📘 Project Overview  
This project demonstrates a complete end-to-end custom data processing and analytics pipeline designed to analyze Netflix user behavior.
Unlike typical dashboards built using Pandas or SQL engines, this project implements a fully custom data-processing framework that handles:
- CSV parsing
- DataFrame manipulation
- Filtering, projection, joins
- GroupBy and aggregation
- Interactive data visualization through a Streamlit dashboard

The implementation highlights an in-depth understanding of data engineering fundamentals and satisfies academic requirements for building low-level data systems from scratch.

---
## 🎯 Objectives

The primary academic objectives include:

1. Implementing a custom DataFrame engine without Pandas.
2. Designing algorithms for:
	- CSV parsing
	- Filtering and selection
	- GroupBy and aggregations
	- Join operations
3. Building an interactive streaming dashboard for:
	- Genre and regional analytics
 	- Rating Distribution
	- Movie insights
	- Top Rated Movies
	- Dynamic Filtering based on Country and Genre

Demonstrating a complete workflow from **raw data → processing → analysis → insights**.

---

## 🧱 Project Structure 
```
Netflix-User-Behavior-Analytics-using-Custom-Data-Processing-System/
│
├── data/						# Netflix's data in CSV format
│   ├── movies.csv
│   ├── reviews.csv
│
├── my_pandas/
│   ├── __init__.py
│   ├── core/
│   │   ├── dataframe.py		# Custom DataFrame implementation
│   │   ├── groupby.py			# Custom GroupBy and Aggregation logic
│   │
│   ├── utils/
│       ├── parser.py			# CSV parser
│
├── web.py						# Streamlit dashboard application
├── requirements.txt			# Required libraries
├── .gitignore
└── README.md
```

---

## ▶️ Running the Project

### 1️⃣ Clone the Repository
```
git clone https://github.com/ArinPaul/Netflix-User-Behavior-Analytics-using-Custom-Data-Processing-System.git
cd Netflix-User-Behavior-Analytics-using-Custom-Data-Processing-System
```
### 2️⃣ Install Dependencies
```
pip install -r requirements.txt
```
### 3️⃣ Run the Streamlit Application
```
streamlit run web.py --server.port 8888
```
Open the app in your browser at: 👉 http://localhost:8888

or,

The application is deployed on Streamlit Cloud and can be accessed here: 👉 https://netflix-analytics-dashboard-v1.streamlit.app/

---

## 📂 Dataset

The dataset contains two CSV file:
1. movies.csv - This table contains 1,040 which provides metadata about the content (movies or shows) in the dataset. It gives context to user behavior, and can be joined with user interactions like reviews for analysis.
2. reviews.csv - This table contains 15,450 reviews of users, thus capturing user-to-item interactions in the form of feedback or ratings. It is likely the core behavioral signal data, since it ties users to the movies via their opinions or actions.

---

## 🌍 Features

🎬 Movie Analytics
- Genre-based distribution
- Country of origin visualization

⭐ User Rating Analytics
- Histogram of ratings
- Average rating per movie

🔗 Joined Insights
- Movie + review join
- Top 10 rated movies

---

## 📐 Projection

Displays combinations of any selected fields, such as:

- **Genre**, **Country of Origin**
- **Release Year**, **Primary Genre**
- Any comma-separated selection of fields from the dataset

This allows you to explore multi-attribute distributions and understand how different movie characteristics intersect.

---

## 🔎 Filtering

Replicates the exact logic used in your data-processing pipeline:

- Extracts unique country and genre values for dynamic user selection  
- Filters and aggregates records based on user-defined inputs  
- Performs accurate, case-insensitive string matching  
- Generates visual insights through multiple interactive chart types

---

## 🔢 GroupBy & Aggregation

Powered by the custom MiniDataFrame engine (no pandas):

Supports:
- count
- sum
- mean
- min
- max

---

## 🔗 Custom Join Engine

Custom Join Functionality:
- Supports multiple join types: inner, left, right, and outer  
- Allows users to specify the columns to join on  
- Automatically normalizes strings to ensure consistent key matching  

---

## 🔮 Future Work Ideas
	•	Sentiment analysis on reviews
	•	Viewing pattern forecasting
	•	Export dashboards to PDF reports
	•	Content-based recommendations

---

## 👤 Author

Arin Paul

Master’s in Applied Data Science - USC

---

## 📜 License

For academic and educational use only.

---
