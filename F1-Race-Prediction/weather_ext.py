import pandas as pd
import requests
import time
import random
from lxml import html

# Path to your CSV file

# Load the CSV
print(races)

# Column name that contains Wikipedia links (update if different)
link_column = 'url'

# Function to extract weather using XPath
def get_weather_from_wiki(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise error if failed
        tree = html.fromstring(response.content)
        # Use the provided XPath to get weather data
        time.sleep(random.uniform(1.5, 2))  # polite delay between 1.5-3.5 seconds
        weather = tree.xpath("/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table[1]/tbody/tr[11]/td/text()")
        return weather[0].strip() if weather else "Not found"
    except Exception as e:
        print(f"Error fetching weather from {url}: {e}")
        return "Error"

# Apply the function to each link
races['weather'] = races[link_column].apply(get_weather_from_wiki)

# Save the updated dataframe with weather
races.to_csv("wiki_with_weather.csv", index=False)
print("✅ Weather data scraped and saved to wiki_with_weather.csv")



import pandas as pd
import requests
import random
import time
from lxml import html

# Path to the CSV that already contains weather data
csv_file = "wiki_with_weather.csv"

# Load the CSV
df = pd.read_csv(csv_file)

# Function to extract weather using XPath
def get_weather_from_wiki(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        tree = html.fromstring(response.content)
        weather = tree.xpath("/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table[1]/tbody/tr[11]/td/text()")
        time.sleep(random.uniform(1.5, 3.5))  # polite delay between 1.5-3.5 seconds
        return weather[0].strip() if weather else "Not found"
    except Exception as e:
        print(f"Retry failed for {url}: {e}")
        return "Error"

# Mask for rows that had errors
error_mask = df['weather'].isin(["Error", "Not found"])

# Retry only the error rows
df.loc[error_mask, 'weather'] = df.loc[error_mask, 'url'].apply(get_weather_from_wiki)

# Save the updated DataFrame
df.to_csv("wiki_with_weather_retry.csv", index=False)
print("✅ Retry complete. Data saved to wiki_with_weather_retry.csv")


import pandas as pd
import numpy as np

# Load your file
df = pd.read_csv("wiki_with_weather.csv")

# Categorize weather descriptions
def categorize_weather(description):
    description = str(description).lower()
    if 'snow' in description:
        return 0  # Snowy
    elif 'rain' in description or 'wet' in description:
        return 1  # Rainy
    elif 'cloud' in description or 'overcast' in description:
        return  2 # Cloudy
    elif 'sun' in description or 'clear' in description or 'fine' in description:
        return 3  # Sunny
    else:
        return 1.5  # Unknown

# Apply function and fill NaNs with 0
df['weather_category'] = df['weather'].apply(categorize_weather).fillna(0).astype(int)

# Save to new CSV
df.to_csv("wiki_with_weather_categorized.csv", index=False)

print("File saved as 'wiki_with_weather_categorized.csv'")
print(df)