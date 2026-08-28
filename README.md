# YuvaIntern Week 1 – Data Science Project

## Data Acquisition, Cleaning and Exploratory Data Analysis of Student Performance

This repository contains my Week 1 work for the **Virtual Data Science with Python Apprentice Internship at YuvaIntern**.

### Project workflow

**Data Acquisition → Data Cleaning → Exploratory Data Analysis → Visualization → Insights**

## Internship Details

- **Organization:** YuvaIntern
- **Role:** Virtual Data Science with Python Apprentice Intern
- **Task:** Week 1 – Data Acquisition, Cleaning, and Exploratory Analysis
- **Student:** Keval Prashant Chaudhari

## Dataset

The project uses the **Student Performance** dataset from the UCI Machine Learning Repository.

- Dataset: Student Performance
- Mathematics file: `student-mat.csv`
- UCI dataset ID: 320
- DOI: 10.24432/C5TG7T
- Source: https://archive.ics.uci.edu/dataset/320/student+performance

UCI describes the dataset as student achievement data from two Portuguese schools, collected using school reports and questionnaires. The dataset provides Mathematics and Portuguese subject files. UCI reports no missing values for the dataset.

## Important note about the dataset file

The original UCI dataset is not redistributed in this repository. Download the official `student.zip` from UCI and place the Mathematics file `student-mat.csv` inside:

```text
dataset/student-mat.csv
```

Or run:

```bash
python code/download_dataset.py
```

The script downloads the official UCI archive and extracts the original Mathematics file.

## Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

## Repository Structure

```text
yuvaintern-week1-data-science/
│
├── README.md
├── requirements.txt
│
├── dataset/
│   └── student-mat.csv              # add official UCI file
│
├── code/
│   ├── download_dataset.py
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
```

## Data Cleaning

The analysis checks:

1. Dataset shape
2. Column names
3. Data types
4. Missing values
5. Duplicate rows
6. Numerical ranges

The UCI documentation reports no missing values. The analysis therefore does not artificially create or impute missing values.

## Exploratory Analysis

The report explores:

- Final grade distribution
- Pass/fail summary using G3 >= 10 as an exploratory threshold
- Going-out frequency and mean final grade
- Weekend alcohol-consumption level and mean final grade
- Missing-value status
- Relationships among academic grades

## Visualizations

The repository contains five visualizations used in the report.

## How to Run

1. Install Python 3.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Download the official UCI dataset or run:

```bash
python code/download_dataset.py
```

4. Ensure `dataset/student-mat.csv` exists.
5. Run:

```bash
python code/student_performance_analysis.py
```

## Important Academic Note

This is an exploratory analysis of observational data. The reported relationships do not establish causation. In particular, UCI notes that G3 has a strong correlation with G1 and G2 because G1 and G2 are earlier-period grades for the same course.

## Reference

Cortez, P. (2008). Student Performance [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5TG7T
