# Netflix_Content_Analytics_Dashboard
Interactive Netflix Content Analytics Dashboard built with Python, Streamlit, Plotly, Pandas, and Data Analysis techniques.
# 🎬 Netflix Content Analytics Dashboard

## 📌 Project Overview

The Netflix Content Analytics Dashboard is an end-to-end Data Analytics project that analyzes Netflix's content library using Python. The project covers the complete analytics workflow, including data cleaning, exploratory data analysis (EDA), data visualization, and interactive dashboard development.

The goal of this project is to extract meaningful insights from Netflix content data, identify trends in movies and TV shows, analyze ratings and genres, and visualize content distribution across countries and years.

---

## 🎯 Objectives

* Clean and preprocess raw Netflix data.
* Perform Exploratory Data Analysis (EDA).
* Analyze content trends across years, countries, genres, and ratings.
* Compare Movies and TV Shows on Netflix.
* Create interactive visualizations.
* Build a professional dashboard for business insights.

---

## 📂 Dataset

Dataset: Netflix Titles Dataset

The dataset contains information about Netflix content, including:

* Show ID
* Type (Movie / TV Show)
* Title
* Director
* Cast
* Country
* Date Added
* Release Year
* Rating
* Duration
* Genre
* Description

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Data Analysis

* Pandas
* NumPy

### Data Visualization

* Matplotlib
* Seaborn
* Plotly

### Dashboard Development

* Streamlit

### Version Control

* Git
* GitHub

---

## 🔍 Data Cleaning Process

The following data cleaning operations were performed:

* Removed duplicate records.
* Handled missing values.
* Standardized date formats.
* Extracted year, month, and day from the date_added column.
* Cleaned movie duration values.
* Verified data types.
* Created analysis-ready datasets.

---

## 📊 Exploratory Data Analysis

The project includes analysis of:

### Content Type Distribution

* Movies vs TV Shows

### Rating Distribution

* Analysis of content ratings such as TV-MA, TV-14, PG, and others.

### Top Countries

* Countries producing the highest number of Netflix titles.

### Genre Analysis

* Most popular genres available on Netflix.

### Content Growth Trends

* Number of titles added to Netflix over time.

### Movie Duration Analysis

* Distribution of movie durations.

---

## 📈 Interactive Dashboard Features

The Streamlit dashboard provides:

* KPI Cards

  * Total Titles
  * Total Movies
  * Total TV Shows
  * Total Ratings

* Interactive Filters

  * Content Type
  * Rating
  * Release Year

* Visualizations

  * Movies vs TV Shows Distribution
  * Rating Distribution
  * Top Countries
  * Top Genres
  * Content Added Over Time
  * Movie Duration Distribution

* Download Filtered Data Feature

---

## 📁 Project Structure

Netflix_Content_Analytics_Dashboard/

├── data/

│ ├── netflix_titles.csv

│ └── netflix_cleaned.csv

├── data_cleaning.ipynb

├── analysis.ipynb

├── app.py

├── .streamlit/

│ └── config.toml

├── requirements.txt

└── README.md
---

## 🚀 How to Run the Project

### Clone Repository

git clone https://github.com/zunaira1607/Netflix_Content_Analytics_Dashboard.git

### Install Dependencies

pip install -r requirements.txt

### Run Dashboard

streamlit run app.py

---

## 📷 Dashboard Preview

Add screenshots of your dashboard here.

Example:

screenshots/dashboard_home.png
<img width="950" height="350" alt="Dashboard1" src="https://github.com/user-attachments/assets/314f5896-78cd-4c55-aedd-73ad5fbe7e98" />
<img width="953" height="388" alt="Dashboard2" src="https://github.com/user-attachments/assets/e39ce620-9034-4810-84c2-836d9c713047" />
<img width="953" height="454" alt="Dashboard3" src="https://github.com/user-attachments/assets/3ea63f91-71cd-4cd4-ba6c-a96390c4b393" />
<img width="959" height="455" alt="Dashboard4" src="https://github.com/user-attachments/assets/00b1b7f9-4a31-46d8-8507-b9bfe5ae96d5" />


---

## 💡 Key Insights

* Movies represent a larger share of Netflix content than TV Shows.
* Certain countries dominate Netflix content production.
* Drama and International content are among the most common genres.
* Netflix content additions increased significantly in recent years.
* Most movies fall within a common duration range, indicating standard content length patterns.

---

## 👩‍💻 Author

**Zunaira Sanober**

Aspiring Data Analyst skilled in Python, SQL, Excel, Power BI, Tableau, and Data Visualization.
