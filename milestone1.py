# -*- coding: utf-8 -*-
"""milestone1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1oT4ftI4uw64-PtpB0o480yCW71C0rh0z
"""

!pip install kaggle -qq
!pip install dash -qq
!pip install gdown -qq

import dash
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from dateutil.relativedelta import relativedelta
import os
import json
import requests
import io
import gdown
import seaborn as sns

from matplotlib import pyplot as plt
from scipy import stats
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
from dash import dash_table

config_dir = '/root/.config/kaggle'
os.makedirs(config_dir, exist_ok=True)

kaggle_json = {
    "username": "ckcchamp",
    "key": "438acc2af14cd41abba475f675733b38"
}
kaggle_json_path = os.path.join(config_dir, 'kaggle.json')
with open(kaggle_json_path, 'w') as f:
    json.dump(kaggle_json, f)
os.chmod(kaggle_json_path, 0o600)

import kaggle

kaggle.api.authenticate()

kaggle.api.dataset_download_files('dtrade84/madden-24-player-ratings',path= '.',unzip=True)
kaggle.api.dataset_download_files('reinerjasin/nba-2k25-player-complete-dataset',path= '.',unzip=True)
kaggle.api.dataset_download_files('rajatsurana979/fifafcmobile24',path= '.',unzip=True)

url = 'https://drive.google.com/uc?export=download&id=1Rlz_djH1iBp6t4GbEPP8UJzE2-Kmh5nH'
gdown.download(url, 'nfl_salary.xlsx')

nfl_salary_raw = pd.read_excel('nfl_salary.xlsx')
nfl_raw = pd.read_csv('maddennfl24fullplayerratings.csv')
nba_raw = pd.read_csv('current_nba_players.csv')
fifa_raw = pd.read_csv('male_players.csv')

def feet_inches_to_cm(height_str):
    try:
        if pd.isna(height_str):
            return None
        height_str = str(height_str).replace(' ', '').replace('"', '')
        parts = height_str.split("'")
        feet = float(parts[0])
        inches = float(parts[1]) if len(parts) > 1 and parts[1] else 0
        total_inches = feet * 12 + inches
        cm = total_inches * 2.54
        return round(cm)
    except:
        return None

def lbs_to_kg(weight_lbs):
    if pd.isna(weight_lbs):
            return None
    weight = pd.to_numeric(weight_lbs, errors='coerce')
    if pd.isna(weight):
            return None
    weight_kg = weight * 0.45359237
    return round(weight_kg)

def inches_to_cm(Height):
    if pd.isna(Height):
            return None
    Height = pd.to_numeric(Height, errors='coerce')
    if pd.isna(Height):
            return None
    height_cm = Height * 2.54
    return round(height_cm)

nfl = nfl_raw[['Full Name', 'Overall Rating', 'Height','Years Pro', 'Weight', 'Age']]
nfl = nfl.merge(
    nfl_salary_raw,
    left_on='Full Name',
    right_on='Player',
    how='inner')

if not pd.api.types.is_numeric_dtype(nfl['APY']):
    nfl['APY'] = nfl['APY'].replace('[\$,]', '', regex=True).astype(float)
nfl.sort_values('APY', ascending=False, inplace=True)
nfl.drop_duplicates('Full Name', keep='first', inplace=True)
nfl=nfl[['Full Name', 'Overall Rating', 'Height', 'Weight', 'Age','Years Pro', 'Pos.', 'APY']]
nfl

nfl['height_cm'] = nfl['Height'].apply(inches_to_cm)
nfl['weight_kg'] = nfl['Weight'].apply(lbs_to_kg)
nfl.drop(['Height', 'Weight'], axis=1, inplace=True)
nfl.rename(columns={'Full Name': 'name', 'Overall Rating': 'overall', 'Years Pro': 'years_pro', 'Pos.': 'position'}, inplace=True)
nfl= nfl[['name', 'overall', 'height_cm', 'weight_kg', 'Age', 'years_pro', 'position', 'APY']]
nfl

target_date = pd.to_datetime('2024-08-30')
nba_raw['Age'] = pd.to_datetime(nba_raw['birthdate'], errors='coerce').apply(
    lambda x: relativedelta(target_date, x).years if pd.notnull(x) else None)
nba = nba_raw[['name', 'overall','height_feet', 'weight_lbs', 'Age','years_in_the_nba', 'position_1', 'season_salary']]
nba

nba['height_cm'] = nba['height_feet'].apply(feet_inches_to_cm)
nba['weight_kg'] = nba['weight_lbs'].apply(lbs_to_kg)
nba['APY']=nba['season_salary']
nba.drop(['height_feet', 'weight_lbs','season_salary'], axis=1, inplace=True)
nba.dropna(subset=['APY'], inplace=True)
nba.rename(columns={'Full Name': 'name', 'years_in_the_nba': 'years_pro', 'position_1': 'position'}, inplace=True)
nba= nba[['name', 'overall', 'height_cm', 'weight_kg', 'Age', 'years_pro', 'position', 'APY']]
nba

fifa = fifa_raw[fifa_raw['fifa_version'] == 24][['long_name', 'overall', 'height_cm','weight_kg', 'age', 'league_level','player_positions', 'wage_eur']]
fifa.drop_duplicates('long_name', keep='first', inplace=True)
fifa = fifa[fifa['league_level'] == 1]
fifa['Age'] = fifa['age']
fifa.drop('age', axis=1, inplace=True)
fifa

def wage_to_salary(wage_eur):
  return wage_eur*52

fifa['APY'] = fifa['wage_eur'].apply(wage_to_salary)
fifa.drop('wage_eur', axis=1, inplace=True)
fifa.rename(columns={'long_name': 'name',  'player_positions': 'position'}, inplace=True)
fifa= fifa[['name', 'overall', 'height_cm', 'weight_kg', 'Age', 'position', 'APY']]
fifa

nfl['sport'] = 'NFL'
nba['sport'] = 'NBA'
fifa['sport'] = 'FIFA'
all_data = pd.concat([nfl, nba, fifa], ignore_index=True)
all_data

for sport in ['NFL', 'NBA', 'FIFA']:
    print(f"\nStats for {sport}:")
    sport_data = all_data[all_data['sport'] == sport]
    print(sport_data[['height_cm', 'weight_kg', 'Age', 'overall', 'APY']].describe().round(2))

def plot_physical_attributes(df):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    sns.boxplot(x='sport', y='height_cm', data=df, ax=ax1)
    ax1.set_title('Height Distribution by Sport')
    ax1.set_ylabel('Height (cm)')

    sns.boxplot(x='sport', y='weight_kg', data=df, ax=ax2)
    ax2.set_title('Weight Distribution by Sport')
    ax2.set_ylabel('Weight (kg)')

    plt.tight_layout()
    plt.show()

plot_physical_attributes(all_data)

def plot_salary_distribution(df):
    plt.figure(figsize=(12, 6))

    for sport in df['sport'].unique():
        sport_data = df[df['sport'] == sport]['APY']
        sns.kdeplot(data=np.log10(sport_data), label=sport)

    plt.title('Salary Distribution (Log Scale)')
    plt.xlabel('Log10(Annual Pay)')
    plt.ylabel('Density')
    plt.legend()
    plt.show()

plot_salary_distribution(all_data)

def plot_performance_comparison(df):
    plt.figure(figsize=(10, 6))

    sns.violinplot(x='sport', y='overall', data=df)
    plt.title('Performance Ratings Distribution by Sport')
    plt.ylabel('Overall Rating')

    plt.show()

plot_performance_comparison(all_data)

def plot_age_experience_analysis(df):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    sns.boxplot(x='sport', y='Age', data=df, ax=ax1)
    ax1.set_title('Age Distribution by Sport')
    for sport in df['sport'].unique():
        sport_data = df[df['sport'] == sport]
        ax2.scatter(sport_data['years_pro'], np.log10(sport_data['APY']),
                   alpha=0.5, label=sport)

    ax2.set_title('Experience vs Salary')
    ax2.set_xlabel('Years Pro')
    ax2.set_ylabel('Log10(Annual Pay)')
    ax2.legend()
    plt.tight_layout()
    plt.show()

plot_age_experience_analysis(all_data)

def plot_correlation_matrix(df):
    numeric_cols = ['height_cm', 'weight_kg', 'Age', 'overall', 'APY']
    for sport in df['sport'].unique():
        plt.figure(figsize=(10, 8))
        sport_data = df[df['sport'] == sport][numeric_cols]
        corr = sport_data.corr()
        sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
        plt.title(f'Correlation Matrix - {sport}')
        plt.show()

plot_correlation_matrix(all_data)

for sport in all_data['sport'].unique():
    print(f"\nTop 5 highest paid {sport} players:")
    top_players = all_data[all_data['sport'] == sport].nlargest(5, 'APY')
    print(top_players[['name', 'position', 'overall', 'APY']].to_string())

for sport in all_data['sport'].unique():
    print(f"\nAverage metrics by position for {sport}:")
    pos_stats = all_data[all_data['sport'] == sport].groupby('position').agg({
        'height_cm': 'mean',
        'weight_kg': 'mean',
        'overall': 'mean',
        'APY': 'mean'
    }).round(2)
    print(pos_stats.to_string())

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('different between Sports'),

    html.Div([
        html.Label('X'),
        dcc.Dropdown(
            id='x-axis',
            options=[
                {'label': 'height(cm)', 'value': 'height_cm'},
                {'label': 'weight(kg)', 'value': 'weight_kg'},
                {'label': 'age', 'value': 'Age'},
                {'label': 'Overall', 'value': 'overall'},
                {'label': 'Salary', 'value': 'APY'}
            ],
            value='height_cm'
        ),

        html.Label('Y'),
        dcc.Dropdown(
            id='y-axis',
            options=[
                {'label': 'height(cm)', 'value': 'height_cm'},
                {'label': 'weight(kg)', 'value': 'weight_kg'},
                {'label': 'age', 'value': 'Age'},
                {'label': 'Overall', 'value': 'overall'},
                {'label': 'Salary', 'value': 'APY'}
            ],
            value='weight_kg'
        ),

        html.Label('Sport'),
        dcc.Checklist(
            id='sport-selector',
            options=[
                {'label': 'NFL', 'value': 'NFL'},
                {'label': 'NBA', 'value': 'NBA'},
                {'label': 'FIFA', 'value': 'FIFA'}
            ],
            value=['NFL', 'NBA', 'FIFA']
        )
    ]),

    # Graph
    dcc.Graph(id='scatter-plot')
])

# Callback to update the graph
@app.callback(
    Output('scatter-plot', 'figure'),
    [Input('x-axis', 'value'),
     Input('y-axis', 'value'),
     Input('sport-selector', 'value')]
)
def update_graph(x_axis, y_axis, selected_sports):
    filtered_data = all_data[all_data['sport'].isin(selected_sports)]

    fig = px.scatter(
        filtered_data,
        x=x_axis,
        y=y_axis,
        color='sport',
        hover_data=['name', 'position', 'Age', 'overall', 'APY'],
        title=f' {x_axis} vs {y_axis}'
    )

    if x_axis == 'APY':
        fig.update_xaxes(type='log')
    if y_axis == 'APY':
        fig.update_yaxes(type='log')

    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

