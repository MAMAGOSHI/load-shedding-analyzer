# Load Shedding Analyzer

## Overview

This project is a Python-based data analysis tool that explores historical electricity and load-shedding data in South Africa. The goal of the project is to better understand trends in electricity supply and visualise patterns within the dataset using graphs and basic analysis techniques.

The project was built as part of my learning journey in data analytics and Python programming. It combines real-world data with practical programming concepts such as data loading, exception handling, data visualisation, and file management.

The dataset used in this project contains historical Eskom electricity and load-shedding information sourced from Kaggle.

---

## Project Objectives

The main objectives of this project were to:

- Work with a real-world dataset
- Practice reading and analysing CSV data using Pandas
- Learn how to automate chart generation
- Create visual representations of numerical trends
- Understand how to structure a Python project
- Practice using Git and GitHub for version control

---

## Dataset Information

Dataset Source:  
https://www.kaggle.com/datasets/sbonelondhlazi/sa-electricity-historical-data

The dataset includes historical information related to electricity and load-shedding trends in South Africa. The data is stored in CSV format and is processed using Python.

---

## Technologies Used

This project was built using:

- Python
- Pandas
- Matplotlib
- Git
- GitHub
- Visual Studio Code

---

## How to Run This Project

Follow these steps to clone and run the project on your own machine.

**1. Clone the repository**
```bash
git clone https://github.com/MAMAGOSHI/load-shedding-analyzer.git
cd load-shedding-analyzer
```

**2. Create and activate a virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Install required packages**
```bash
pip install -r requirements.txt
```

**4. Set up your Kaggle API credentials**

- Go to kaggle.com and log in
- Click your profile picture and go to Settings
- Under API click Create New Token
- This downloads kaggle.json to your Downloads folder
- Run these commands in your terminal:

```bash
mkdir -p ~/.kaggle
mv ~/Downloads/kaggle.json ~/.kaggle/kaggle.json
chmod 600 ~/.kaggle/kaggle.json
```

**5. Run the program**
```bash
python main.py
```

Charts will be saved automatically to the `charts/` folder.

---

## How the Project Works

The program begins by loading the dataset from the local data folder using Pandas. Once the data has been loaded successfully, the program identifies numeric columns within the dataset and uses them for analysis and visualisation.

Matplotlib is used to generate charts that display trends within the data. The generated charts are automatically saved as PNG image files inside the charts folder.

The project also includes basic exception handling to manage possible errors such as missing files or invalid data paths.

---

## Analysis Questions and Findings

### Q1 — What is the average load shedding stage per month?

Looking at the data grouped by month, the average stage varies throughout the year. Months in the middle of the year consistently show higher average stages compared to summer months. This suggests that load shedding is not evenly distributed across the year.

### Q2 — Which months or seasons see the most severe stages? Does the data support the claim that winter is worst?

The data does support this claim. Winter months — June, July and August — show the highest average load shedding stages. This aligns with increased electricity demand during cold weather when households use more heating. Summer months like December and January show lower average stages, confirming that winter is the peak period for severe load shedding.

### Q3 — Is there a day-of-week pattern? Are weekdays different from weekends?

The analysis shows a slight pattern where weekdays have a marginally different average stage compared to weekends. This could be explained by industrial and commercial electricity demand being higher on weekdays when businesses are operating. However the difference is not dramatic — load shedding affects all days of the week.

### Q4 — How many total hours of outages occurred per year? Show the trend.

The total outage hours increased significantly in more recent years in the dataset. Earlier years show lower totals while later years show a clear upward trend. This reflects the well-known worsening of South Africa's load shedding crisis over time as Eskom's generation capacity declined.

### Q5 — Open-ended insight

My open-ended insight looked at the frequency of severe stages — stage 4 and above — per year. The data shows that severe stages were rare in earlier years but became increasingly common in more recent years. This means South Africans are not just experiencing more outages but more intense ones. Stage 4 and above means up to 12 hours of no electricity per day, which has a serious impact on businesses, households and the economy.

---

## Visualisations

### Stage Over Time
![Stage Over Time](charts/stage_over_time.png)

### Average Stage by Month
![Average Stage by Month](charts/avg_stage_by_month.png)

### Average Stage by Day of Week
![Average Stage by Day](charts/stage_by_day.png)

---

## Lessons Learned

- I learned how to structure a Python project as a package using separate modules for loading, cleaning, analysing and visualising data
- I learned how to use the Kaggle API to download datasets programmatically instead of downloading manually
- I learned how to use Pandas to group and aggregate data to answer real questions
- I learned how to use Matplotlib to generate and save charts automatically
- I learned the importance of exception handling — without it, errors are confusing and hard to debug
- I learned how to use Git properly with meaningful commit messages to show the progression of my work
- Working with a real dataset taught me that data is never perfect — there are always missing values, duplicates and formatting issues that need to be cleaned before analysis can begin


