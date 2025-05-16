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

print(results_df.columns)

# Extract only relevant information about the race for training purposes
race_df = races[["raceId", "year", "round", "circuitId"]].copy()