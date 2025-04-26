# Athlete Career Prediction Dashboard

An interactive data science project to predict and compare potential athletic career outcomes across multiple professional sports leagues based on physical attributes.

## Project Overview

This project helps young athletes make more informed career decisions by analyzing data from three major sports leagues (NFL, NBA, and FIFA). The dashboard allows users to input their physical attributes and see predicted performance and earnings across different sports, helping to identify which sport might offer the best career path given their natural physical characteristics.

## Data Sources

The project leverages sports video game data which provides accurate and up-to-date player statistics:

### American Football: Madden NFL 24 Player Ratings

- Source: Kaggle Dataset
- Features: Height, Weight, Speed, Strength, Position, Overall Rating

### Basketball: Complete NBA 2K25 Player Dataset

- Source: Kaggle Dataset
- Features: Height, Weight, Salary, Position, Overall Rating, Potential

### Soccer: FIFA Mobile FC-24

- Source: Kaggle Dataset
- Features: Height, Weight, Position, Overall Rating, Market Value

### NFL Contracts: Supplementary salary data from Over The Cap

- Source: Over The Cap

## Installation and Setup

### Prerequisites

- Python 3.8 or higher
- Git (for cloning the repository)
- Internet connection (for downloading model files if not included)

### Step-by-Step Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/athlete-career-prediction.git
cd athlete-career-prediction
```

2. Create a virtual environment (recommended)
```bash
# Using venv
python -m venv venv

# Activate the environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install required packages
```bash
pip install -r requirements.txt
```

If the requirements.txt file is not available, install the necessary packages manually:
```bash
pip install dash pandas numpy plotly matplotlib seaborn scikit-learn tensorflow joblib gdown
```

4. Download model files (if not included)
Make sure the following model files are in the project root directory:

- fifa_model.joblib
- nba_model.joblib
- nfl_model.joblib

If models are missing, the application will display appropriate error messages.

### Running the Dashboard

1. Launch the application
```bash
python milestone3.py
```

2. Access the dashboard
Open a web browser and navigate to:
http://127.0.0.1:8050/

The dashboard should load in your default web browser. If there are any port conflicts, check the console output for the correct URL.

## Using the Dashboard

The dashboard is organized into several sections that allow for interactive exploration of potential career paths:

### 1. Shared Athlete Metrics

This top section allows you to input your physical attributes:

- Height Slider: Adjust to set your height in centimeters (150-230 cm)
- Weight Slider: Adjust to set your weight in kilograms (50-150 kg)
- Age Slider: Adjust to set your current age (16-40 years)
- BMI Display: Automatically calculated based on your height and weight

These values are shared across all sport predictions, allowing for easy comparison.

### 2. Sport-Specific Panels

#### NBA Panel

- Years Professional Slider: Adjust to set how many years you've been playing professionally (0-20)
- Position Dropdown: Select your basketball position:
  - Point Guard (PG)
  - Shooting Guard (SG)
  - Small Forward (SF)
  - Power Forward (PF)
  - Center (C)
- Age Entered Pro Display: Automatically calculated based on your age and years pro
- Predict Button: Click to generate NBA career predictions based on your inputs

#### NFL Panel

- Years Professional Slider: Adjust to set how many years you've been playing professionally (0-20)
- Position Dropdown: Select your football position from the 8 consolidated position groups:
  - Quarterback (QB)
  - Receiver (includes WR and TE)
  - Defensive Line (DL)
  - Offensive Line (OL)
  - Defensive Back (DB)
  - Linebacker (LB)
  - Running Back (RB)
  - Specialist (includes K, P, LS)
- Age Entered Pro Display: Automatically calculated based on your age and years pro
- Predict Button: Click to generate NFL career predictions based on your inputs

#### FIFA Panel

- Predict Button: Click to generate FIFA career predictions based on your inputs
- Note: FIFA predictions rely only on physical attributes and age (no position or years pro input required)

### 3. Prediction Results

For each sport, after clicking the predict button, the dashboard will display:

- Career Trajectory Chart: Shows predicted overall rating changes over the next 10 years
- Statistical Summary:
  - Initial Rating
  - Peak Rating (with age at peak highlighted)
  - Final Rating (with change from initial rating)
- Model Interpretation: Text explanation of your predicted career path

Note: All predictions assume height and weight remain constant, only considering changes in age and experience

## Example Workflow

1. Input your physical metrics:
   - Set Height: 190 cm
   - Set Weight: 85 kg
   - Set Age: 22

2. Generate NBA Prediction:
   - Set Years Pro: 1
   - Select Position: PG
   - Click "Predict NBA 10-Year Career Changes"
   - Review your predicted trajectory

3. Generate NFL Prediction:
   - Set Years Pro: 1
   - Select Position: QB
   - Click "Predict NFL 10-Year Career Changes"
   - Review your predicted trajectory

4. Generate FIFA Prediction:
   - Click "Predict FIFA 10-Year Career Changes"
   - Review your predicted trajectory

5. Compare Results: Analyze which sport shows the highest potential based on:
   - Highest peak rating
   - Longest prime years
   - Most favorable career trajectory

## Interpreting Results

- Overall Rating: A normalized score (0-100) representing player ability
- Career Trajectory: Shows how your performance is likely to develop over time
- Peak Rating: Indicates your maximum potential and at what age you'll reach it
- Comparing Sports: Higher ratings or longer peaks in one sport suggest better natural fit

## Troubleshooting

### Common Issues

- Dashboard doesn't load:
  - Check that all required packages are installed
  - Ensure port 8050 isn't in use by another application
  - Try running with a different port: python milestone3.py --port 8051

- Models fail to load:
  - Verify model files exist in the project directory
  - Re-run milestone2.py to regenerate models if missing
  - Check console output for specific error messages

- Predictions not appearing:
  - Verify all inputs have valid values
  - Check browser console for JavaScript errors
  - Try clicking the prediction button again

- Visualizations not rendering:
  - Update Plotly: pip install plotly --upgrade
  - Try a different web browser
  - Clear browser cache and reload

### Technical Support

If you encounter persistent issues:

- Check the console output for error messages
- Verify all dependencies are correctly installed
- Ensure you have sufficient memory to run the dashboard

## Development and Customization

### Adding New Sports

To add a new sport to the dashboard:

1. Collect player data with relevant attributes
2. Create a new model in milestone2.py following the existing pattern
3. Add a new sport panel in milestone3.py
4. Update the callback functions to handle the new sport

### Updating Models

If you want to update the machine learning models:

1. Modify the model training code in milestone2.py
2. Run the script to generate new model files
3. Replace the existing model files with the new ones

### Customizing the UI

To modify the dashboard appearance:

1. Update the CSS styles in the colors dictionary in milestone3.py
2. Modify the layout components in each panel creation function
3. Add or remove dashboard elements by editing the app.layout

## Project Structure

The project is organized into three main milestones:

### Milestone 1: Data Collection, Preprocessing, and EDA

- Data acquisition from Kaggle and external sources
- Standardization of measurements (height in cm, weight in kg)
- Exploratory data analysis of physical attributes and salaries across sports

### Milestone 2: Feature Engineering, Selection, and Modeling

- Creation of derived features (BMI, age entered professional leagues)
- Position encoding for cross-sport comparison
- Development and evaluation of multiple regression models

### Milestone 3: Interactive Dashboard Development

- Implementation of a Dash web application
- Integration of trained models for real-time prediction
- Visualization of career trajectories and comparisons

## Technologies Used

- Data Processing: Pandas, NumPy
- Visualization: Matplotlib, Seaborn, Plotly
- Machine Learning: Scikit-learn, TensorFlow
- Model Persistence: Joblib
- Dashboard: Dash, HTML, CSS
- API Integration: Kaggle API, GDown

## Contributing

Contributions to improve the project are welcome:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is available for educational purposes. All data sources are publicly accessible and used in compliance with their respective terms of use.

## Author

Kuan-Chen Chen

Feel free to reach out with any questions or suggestions for improvement!