
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, RidgeCV, LassoCV, ElasticNetCV
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.preprocessing import StandardScaler
from scipy.stats import norm
import kagglehub

# Download dataset
folder_path = kagglehub.dataset_download("rohanrao/formula-1-world-championship-1950-2020")

# Load data
results = pd.read_csv(folder_path + "/" +"results.csv")
races = pd.read_csv(folder_path + "/" +"races.csv")
qualifying = pd.read_csv(folder_path + "/" +"qualifying.csv")
pit_stops = pd.read_csv(folder_path + "/" +"pit_stops.csv")
constructor_standings = pd.read_csv(folder_path + "/" +"constructor_standings.csv")
constructors = pd.read_csv(folder_path + "/" +"constructors.csv")
drivers = pd.read_csv(folder_path + "/" +"drivers.csv")
status = pd.read_csv(folder_path + "/" +"status.csv")

# Constructor standings
constructor_standings_latest = constructor_standings.sort_values(by=['raceId', 'points'], ascending=[True, False])
constructor_standings_latest = constructor_standings_latest.drop_duplicates(subset=['raceId', 'constructorId'])
constructor_standings_latest = constructor_standings_latest.merge(
    constructors[['constructorId', 'name']], on='constructorId', how='left'
).rename(columns={'name': 'constructor_name'})

results = results.merge(
    constructors[['constructorId', 'name']], on='constructorId', how='left'
).rename(columns={'name': 'constructor_name'})
results = results.merge(
    constructor_standings_latest[['raceId', 'constructorId', 'points']],
    on=['raceId', 'constructorId'], how='left'
).rename(columns={'points': 'constructor_standing_points'})
results = results.merge(races[['raceId', 'year', 'round', 'name', 'date', 'circuitId']], on='raceId', how='left')

# Pit stop duration
pit_stops['duration'] = pd.to_numeric(pit_stops['duration'], errors='coerce')
pit_stop_time = pit_stops.groupby(['raceId', 'driverId'])['duration'].sum().reset_index()
pit_stop_time = pit_stop_time.rename(columns={'duration': 'total_pit_stop_time'})

# Constructor points merge
constructor_standings = constructor_standings.merge(constructors[['constructorId', 'name']], on='constructorId', how='left')
constructor_standings.rename(columns={'name': 'constructor_name'}, inplace=True)
results = results.merge(constructor_standings[['raceId', 'constructor_name', 'points']],
                        on=['raceId', 'constructor_name'], how='left', suffixes=('', '_dup'))
results.drop(columns=['points_dup'], errors='ignore', inplace=True)

# Absolute skill
results = results.sort_values(by=['driverId', 'year', 'round'])
results['cumulative_points'] = results.groupby('driverId')['points_x'].cumsum() - results['points_x']
results['races_so_far'] = results.groupby('driverId').cumcount()
results['avg_driver_points'] = results['cumulative_points'] / results['races_so_far'].replace(0, 1)

# Pit stop rate
avg_pit_rate = pit_stops.groupby('raceId')['stop'].nunique().reset_index()
avg_pit_rate = avg_pit_rate.merge(races[['raceId', 'circuitId']], on='raceId', how='left')
track_pit_rate = avg_pit_rate.groupby('circuitId')['stop'].mean().reset_index()
track_pit_rate.rename(columns={'stop': 'avg_pit_stops_per_race'}, inplace=True)

# DNF rate
results = results.merge(status, on='statusId', how='left')
results['dnf'] = results['status'].apply(lambda x: 1 if x != 'Finished' else 0)
dnf_rate = results.groupby('circuitId')['dnf'].mean().reset_index()
dnf_rate.rename(columns={'dnf': 'avg_dnf_rate'}, inplace=True)

# Feature assembly
features = results.merge(pit_stop_time, on=['raceId', 'driverId'], how='left')
features = features.merge(track_pit_rate, on='circuitId', how='left')
features = features.merge(dnf_rate, on='circuitId', how='left')
grid_data = results[['raceId', 'driverId', 'grid']]
features = features.merge(grid_data, on=['raceId', 'driverId'], how='left')
features['grid'] = results['grid']

final_features = features[[
    'raceId', 'driverId', 'constructorId', 'points_x',
    'total_pit_stop_time', 'constructor_standing_points', 'grid',
    'avg_driver_points', 'avg_pit_stops_per_race', 'avg_dnf_rate'
]].dropna()
final_features = final_features.rename(columns={'points_x': 'target_points'})

# Merge weather
races_filtered = races
valid_race_ids = races_filtered['raceId'].unique()
final_features = final_features[final_features['raceId'].isin(valid_race_ids)].reset_index(drop=True)
final_features = final_features.drop(columns=['year', 'year_x', 'year_y'], errors='ignore')
final_features = final_features.merge(races_filtered[['raceId', 'year']], on='raceId', how='left')

weather_data = pd.read_csv("wiki_with_weather_categorized.csv")[['raceId', 'weather_category']]
final_features = final_features.drop(columns=['weather_category', 'weather_category_x', 'weather_category_y'], errors='ignore')
final_features = final_features.merge(weather_data, on='raceId', how='left')
final_features['weather_category'] = final_features['weather_category'].fillna(1.5)

# Save
final_features.to_csv("f1_final_features.csv", index=False)

# Regression model training
train_data = final_features[(final_features['year'] >= 2011) & (final_features['year'] <= 2017)]
test_data = final_features[(final_features['year'] >= 2018) & (final_features['year'] <= 2020)]

X_train = train_data.drop(columns=['target_points', 'year'])
y_train = train_data['target_points']
X_test = test_data.drop(columns=['target_points', 'year'])
y_test = test_data['target_points']
X_test['year'] = test_data['year'].values  # Add year back for plotting

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Results
print("R² Score:", r2_score(y_test, y_pred))
print("MAE:", mean_absolute_error(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))

# Plot: Actual vs Predicted
plt.figure(figsize=(14, 6))
plt.plot(y_test.values, label='Actual Points', color='green', marker='o')
plt.plot(y_pred, label='Predicted Points', color='red', marker='x')
plt.xlabel("Sample Index")
plt.ylabel("Points")
plt.title("Actual vs Predicted Points")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()