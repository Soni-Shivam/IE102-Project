# Formula 1 Race Performance Prediction Model

## Project Overview
This project was a part of my course project IE102 - Probability and Statistics Course in my freshman year. We were assigned an open ended topic where we could build a project upon any topic related to the subjects we studied in this course. This project's main objective was to get a hand on experience at Linear Regression. This project aims to predict Formula 1 race performance by analyzing historical race data and various performance indicators. The model uses multi variable linear regression to predict the points a driver might score in a race based on multiple factors including qualifying position, team performance, weather conditions, and track characteristics.

## Documentation
The complete documentation of the project can be found [here](https://docs.google.com/document/d/e/2PACX-1vSYFxjFkRq2OfeOxZKt3Vj2irzQyRKWgNlc9Kmtgc1QL6VgJ4ApefXbqTSbv2AJrdHacDBZzx1cgRvu/pub).

## Problem Statement
Formula 1 racing is a complex sport where multiple factors influence a driver's performance. The challenge is to:
- Predict race outcomes based on historical data
- Understand the impact of various factors on race performance
- Create a model that can be used for race strategy and performance analysis

## Data Sources
The project utilizes the following datasets from Kaggle:
- Formula 1 World Championship (1950-2020) dataset on Kaggle
- Additional weather data categorized for each race, found out by web scraping on Wikipedia and classifying them into categories

## Features Used
The model incorporates several key features:
1. **Qualifying Performance**
   - Grid position
   - Qualifying times

2. **Team Performance**
   - Constructor standing points
   - Historical team performance

3. **Track Characteristics**
   - Average pit stops per race
   - Track difficulty (measured by DNF rate)
   - Circuit-specific statistics

4. **Weather Conditions**
   - Weather categories for each race
   - Historical weather impact on performance on a driver

5. **Driver Statistics**
   - Average driver points
   - Historical performance metrics

## Methodology

### Data Processing
1. Data cleaning and preprocessing
2. Feature engineering
3. Handling missing values
4. Data normalization

### Model Development
- Multi Linear Regression model
- Training period: 2011-2017
- Testing period: 2018-2020
- Cross-validation for model robustness

### Performance Metrics
- R² Score
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

## Technical Requirements
- Python 3.10+
- Required Libraries:
  - pandas
  - numpy
  - scikit-learn
  - matplotlib
  - seaborn
  - kagglehub

