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

## 🌍 Features

Interactive Map
	•	Auto-detects latitude/longitude columns
	•	Plots up to 5,000 crime locations for performance
	•	Uses Mapbox Light theme
	•	Fully interactive zoom & pan

---

## 🔎 Filtering

Replicates the exact logic used in your Jupyter Notebook:
	•	Exact string match
	•	Case-insensitive
	•	Trims whitespace
	•	Aggregates by AREA NAME
	•	Visualizes using horizontal bar charts

---

## 🔢 GroupBy & Aggregation

Powered by the custom MiniDataFrame engine (no pandas):

Supports:
	•	count
	•	sum
	•	mean
	•	min
	•	max

---

## 📐 Projection

Counts combinations of any selected fields, such as:
	•	AREA NAME, Crm Cd Desc
	•	Any comma-separated list

Displayed via clean horizontal bar charts.

---
## 🔗 Custom Join Engine

Self-join or custom join:
	•	Supports: inner, left, right, outer
	•	Normalizes strings to match keys
	•	Optional suffix handling for duplicate columns

Includes a dedicated Join Visualization tab:
	•	Preview joined rows
	•	Generate co-occurrence heatmaps (e.g., AREA NAME × AREA NAME_R)

---

## 🕒 Crimes Over Time

Uses the processed DATE OCC column to generate:
	•	Daily crime count line chart
	•	Optional smoothed rolling average
	•	Shows long-term temporal behavior trends

---

## 🔥 Temporal Heatmaps

Two modes:

1. Hour × Day of Week (Global)
	•	7 × 24 heatmap
	•	Reveals weekly periodic crime activity

2. Area × Hour Heatmap (Notebook Logic)
	•	Identifies Top N areas
	•	Computes hourly crime frequencies
	•	Displays a vertical heatmap representing peak hours per area

Perfectly replicates your original notebook logic.

---

## 📂 Dataset Requirements

Your dataset must contain:

Mandatory:
	•	DATE OCC
	•	TIME OCC
	•	AREA NAME
	•	Crm Cd Desc
	•	DR_NO

Coordinates: include either
	•	LATITUDE & LONGITUDE
or
	•	a POINT(...) or Location column

The app auto-detects and parses coordinate fields.

---

## 🔮 Future Work Ideas
	•	ML-based crime hotspot prediction
	•	NLP-generated summaries of crime activity
	•	Export dashboards to PDF reports
	•	Interactive GeoJSON grid maps
	•	Integration with Police Beat codes

---

## 👤 Author

Vidit Shah
Master’s in Applied Data Science
LA Crime Analytics Project

---

## 📜 License

For academic and educational use only.
Not intended for operational law-enforcement deployment.

---
