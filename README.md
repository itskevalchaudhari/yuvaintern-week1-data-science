# YuvaIntern Week 1 – Data Science Project

## Data Acquisition, Cleaning and Exploratory Data Analysis of Student Performance

This project was completed as part of the Week 1 task for the
Virtual Data Science with Python Apprentice Internship at YuvaIntern.

The project demonstrates the basic data science workflow:

Data Acquisition → Data Cleaning → Exploratory Data Analysis → Visualization → Insights

---

## Internship Details

- Organization: YuvaIntern
- Internship Role: Virtual Data Science with Python Apprentice Intern
- Task: Week 1 – Data Acquisition, Cleaning, and Exploratory Analysis
- Student: Keval Prashant Chaudhari

---

## Project Objective

The objective of this project is to simulate the data preparation and
exploratory analysis process used in a data science project.

The project focuses on:

- Acquiring a publicly available dataset
- Understanding the dataset structure
- Checking data quality
- Handling missing values
- Checking duplicate records
- Reviewing data types
- Performing exploratory data analysis
- Creating visualizations
- Extracting meaningful insights

---

## Dataset

The dataset used in this project is the Student Performance dataset
from the UCI Machine Learning Repository.

Dataset:
Student Performance – Mathematics (student-mat.csv)

Source:
https://archive.ics.uci.edu/dataset/320/student+performance

The Mathematics dataset contains 395 student records and 33 attributes.

The dataset includes demographic, social, school-related and academic
information.

Important variables include:

- studytime – Weekly study time
- failures – Number of past class failures
- absences – Number of school absences
- G1 – First-period grade
- G2 – Second-period grade
- G3 – Final grade

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

---

## Data Cleaning

The following data-quality checks were performed:

1. Checked dataset dimensions
2. Checked column names
3. Checked data types
4. Checked missing values
5. Checked duplicate records
6. Reviewed numerical ranges

The dataset contained no missing values and no duplicate rows,
so no unnecessary imputation or row deletion was performed.

---

## Exploratory Data Analysis

The analysis explored:

- Distribution of final grades
- Pass/fail distribution based on G3
- Relationship between going-out frequency and final grade
- Relationship between weekend alcohol consumption and final grade
- Missing-value status

---

## Visualizations

The project includes the following visualizations:

1. Final Grade Distribution
2. Pass vs Fail Distribution
3. Going-Out Frequency vs Mean Final Grade
4. Weekend Alcohol Consumption vs Mean Final Grade
5. Missing-Value Check

---

## Key Insights

- The mean final Mathematics grade is approximately 10.42.
- The median final grade is 11.
- Grade 10 is one of the most frequent final-grade values.
- The dataset contains students with final grades ranging from 0 to 20.
- Going-out frequency does not show a simple increasing relationship
  with final grade.
- Weekend alcohol-consumption groups also do not show a simple
  monotonic relationship with final grade.
- No missing values were found in the dataset.
- No duplicate rows were found.

---

## Project Structure

```text
yuvaintern-week1-data-science/
│
├── README.md
│
├── dataset/
│   └── student-mat.csv
│
├── code/
│   └── student_performance_analysis.py
│
├── visualizations/
│   ├── g3_distribution.png
│   ├── pass_fail.png
│   ├── goout_mean.png
│   ├── walc_mean.png
│   └── missing_values.png
│
└── report/
    └── YuvaIntern_Week1_Student_Performance_Report.docx

