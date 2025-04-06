
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
├── milestone1.py          
├── Reports/
│   └── Milestone1.pdf    
├── README.md
```


## Key Features of the Analysis
- Descriptive statistics for athlete attributes
- Physical attribute comparisons across sports
- Salary distribution analysis
- Performance rating comparisons
- Age and experience analysis
- Correlation analysis
- Position-specific insights


## Implemented Features and Methodology

### Data Preprocessing
- **Position Encoding**: Implemented custom mapping systems to consolidate similar positions
  - NBA positions reduced from 5 to 3 categories (Guards, Forwards, Centers)
  - NFL positions reduced from 18 to 8 functional groups
  - FIFA positions handled separately due to positional complexity
- **Feature Engineering**:
  - Added BMI (Body Mass Index) to capture optimal body composition for different sports
  - Created enter_pro feature to track age of entry into professional leagues
  - Standardized numerical features for consistent model training
- **Dataset Enhancement**:
  - Expanded NBA dataset from 399 to 800 players by incorporating NBA 2K20 data
  - Split data into 5 distinct datasets for separate model training

### Model Development
- **Multiple Regression Models**:
  - Linear Models: Linear Regression, Ridge Regression, Lasso Regression
  - Non-Linear Models: Random Forest Regressor, Gradient Boosting Regressor
- **Hyperparameter Optimization**:
  - Implemented GridSearchCV for systematic parameter tuning
  - Optimized parameters include:
    - Tree depths, estimator counts, and learning rates for ensemble methods
    - Regularization strengths for Ridge and Lasso
- **Automated Training Framework**:
  - Developed unified model execution pipeline to streamline experimentation
  - Systematically tracked feature utilization and model performance
  - Implemented standardized evaluation metrics (MSE, RMSE, R² score)

### Key Findings
- **Sport-Specific Best Models**:
  - NBA: Gradient Boosting 
  - NFL: Random Forest 
  - FIFA: Ridge Regression 
- **Physical Attribute Importance**:
  - NBA: Physical attributes less predictive of salary compared to other sports
  - NFL: Strong correlation between physical attributes and earnings, especially for linemen
  - FIFA: Speed and agility-related metrics most valuable across positions
- **Feature Importance Variation**:
  - Height most predictive for NBA centers
  - Weight strongly correlated with NFL salary
  - BMI particularly important for FIFA players
  - Early professional entry age significantly indicative of earning potential in NBA

### Correlation Analysis
- Implemented specialized correlation analysis function (`corr_matrix_plt`)
- Generated correlation heatmaps to visualize feature relationships
- Identified key physical predictors for each sport

## Key Features of the Analysis
- Descriptive statistics for athlete attributes
- Physical attribute comparisons across sports
- Salary distribution analysis
- Performance rating comparisons
- Age and experience analysis
- Correlation analysis
- Position-specific insights
- Predictive modeling of earnings potential based on physical attributes


## Future Development
Upcoming developments include:
- Integration of additional performance metrics
- Development of interactive prediction tool for user input
- Sports-specific career path recommendation system
- Incorporation of historical progression data for early-career projection

## LLM
I use Claude for polishing my reports, helping to correct grammar and enhance readability. Claude also assisted in optimizing the technical writing in the methodology sections.


