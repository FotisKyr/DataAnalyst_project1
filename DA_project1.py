import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
desired_width=720
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns',25)

def read_data():
    df = pd.read_csv('tmdb-movies.csv')
    return df

df = read_data()

# Check for missing values in columns popularity, release year and genres
print(df['genres'].isnull().values.any())
print(df['release_year'].isnull().values.any())
print(df['popularity'].isnull().values.any())

# Drop rows where there is no genre indicated

df = df.dropna(how='any', subset=['genres'])
print(df['genres'].isnull().values.any())DA
# Extract only the first genre title that is considered to be the main title
df['genres'] = df['genres'].str.split('|').str[0]


df_year_genre = df.groupby(['release_year','genres']).popularity.mean()
print(df_year_genre)
