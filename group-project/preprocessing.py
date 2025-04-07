import pandas as pd
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

folder_path = '/home/shivam/code-masala/ieor/data'

# ID of constructors
constructors_df = pd.read_csv(folder_path + '/constructors.csv')

# ID of drivers
drivers_df = pd.read_csv(folder_path + '/drivers.csv')

# ID of each race
races = pd.read_csv(folder_path + '/races.csv')

# Starting grid and final position of every driver in every race (also includes status of each race)
results_df = pd.read_csv(folder_path + '/results.csv')

""" 
pd.get_option("display.max_columns",None)
print(results_df) """

# print(results_df.columns)

# Extract only relevant information about the race for training purposes
race_df = races[["raceId", "year", "round", "circuitId"]].copy()

# After obtaining all relevant information about the race, we can get rid of the raceId variable
race_df = race_df.sort_values(by=['year', 'round'])

#use data from 1982 onwards and before 2022
race_df = race_df[(race_df["year"] >= 1982) & (race_df["year"] <= 2022)]

print(race_df)
# Starting grid and final position of every driver, constructor in every race (also includes status of each race)
print("Driver result of a race")
print(results_df.head())

print("Race_df dataframe")
print(race_df.head())