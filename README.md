
# Athlete Career Path Prediction Project

## Overview
This project aims to help young athletes make data-driven career decisions by analyzing professional athlete data across three major sports: American Football (NFL), Basketball (NBA), and Soccer (FIFA). Using data from modern sports video games and real contract information, we provide insights into how physical attributes correlate with success and earnings in different sports.

## Features
- Analysis of physical attributes (height, weight) across different sports
- Salary distribution comparisons
- Performance rating analysis
- Career trajectory visualization
- Interactive dashboard for data exploration

## Data Sources
The project uses the following datasets:
1. Madden NFL 24 Player Ratings (Kaggle)
2. NBA 2K25 Player Dataset (Kaggle)
3. FIFA Mobile FC-24 (Kaggle)
4. NFL Contracts Data (Over The Cap)

## Prerequisites
- Python 3.8+
- Kaggle account for dataset access
- Required Python packages:
  ```
  pip install pandas numpy matplotlib seaborn dash kaggle gdown
  ```

## Setup
1. Clone the repository
2. Set up Kaggle API credentials:
   - Create a Kaggle account if you don't have one
   - Go to your Kaggle account settings
   - Generate an API token
   - Place the kaggle.json file in the appropriate directory

3. Download the datasets:
   - The script will automatically download Kaggle datasets using the API
   - NFL contracts data will be downloaded using gdown

## Project Structure
```
├── milestone1.py          # Main analysis script
├── Reports/
│   └── Milestone1.pdf    # Detailed report of data collection and analysis
├── README.md
└── requirements.txt
```


## Key Features of the Analysis
- Descriptive statistics for athlete attributes
- Physical attribute comparisons across sports
- Salary distribution analysis
- Performance rating comparisons
- Age and experience analysis
- Correlation analysis
- Position-specific insights

## Future Development
Upcoming milestones include:
- Feature Engineering (Feb 21 - Mar 2)
- Feature Selection (Mar 2 - Mar 7)
- Data Modeling (Mar 8 - Mar 14)
- Final Report (Mar 14 - 20)


## LLM
I use claude for polish my report, I use claude to correct the grammer and made the report more readable

