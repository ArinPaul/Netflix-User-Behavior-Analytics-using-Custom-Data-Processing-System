# Netflix User Behavior Analytics Dashboard
*A Data-Driven Interactive Crime Analysis Tool for Los Angeles*

---

## 📊 Overview  
This project is a **Streamlit-based web application** designed to provide a complete analytical environment for exploring the **Los Angeles Crime Dataset** using a **custom-built MiniDataFrame engine** (your own parser, type-inference, filtering, projection, groupby, aggregation, join logic).

Unlike typical dashboards built with Pandas, this project uses a **pure Python analytical engine** that mirrors your notebook implementation, satisfying academic requirements for:

- Manual CSV parsing  
- Manual type inference  
- Custom filter, groupby, join, aggregation  
- Visualization consistent with notebook output  
- Self-join visualization  
- PyDeck-based geographic mapping  
- Time-series analysis  
- Temporal heatmaps  

---

## 🧱 Project Structure  
Data-Driven-Crime-Analysis/
│
├── app_streamlit.py        # Main Streamlit application
├── data/
│   └── la_crime_data.csv   # LA Crime dataset (not provided publicly)
│
├── src/
│   └── crime_data_processor.py   # MiniDataFrame engine and helpers
│
├── requirements.txt        # Python package dependencies
└── README.md               # Project documentation

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
git clone https://github.com/vidmshah/Data-Driven-Crime-Analysis.git
cd Data-Driven-Crime-Analysis

### 2️⃣ Install Dependencies
pip install -r requirements.txt

### 3️⃣ Run the Streamlit Application
streamlit run app_streamlit.py

Open the app in your browser at:
👉 http://localhost:8501

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
