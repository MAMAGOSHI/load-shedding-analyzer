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

## How the Project Works

The program begins by loading the dataset from the local data folder using Pandas. Once the data has been loaded successfully, the program identifies numeric columns within the dataset and uses them for analysis and visualisation.

Matplotlib is used to generate charts that display trends within the data. The generated charts are automatically saved as PNG image files inside the charts folder.

The project also includes basic exception handling to manage possible errors such as missing files or invalid data paths.
