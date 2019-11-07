import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import ExcelWriter
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
print(df['genres'].isnull().values.any())

# Extract only the first genre title that is considered to be the main title
df['genres'] = df['genres'].str.split('|')

# Make a new row for every element in the genre values list
lst_col = 'genres'
df = pd.DataFrame({col:np.repeat(df[col].values, df[lst_col].str.len()) for col in df.columns.drop(lst_col)}).assign(**{lst_col:np.concatenate(df[lst_col].values)})[df.columns]

# Create dataframe with info on the average popularity of each genre each year
df_year_genre = df.groupby(['release_year','genres'], as_index=False).popularity.mean()
#print(df_year_genre.head(20))

# Extract the max average popularity and the genre type for each year
df_year_genre = df_year_genre.sort_values('popularity', ascending=False).drop_duplicates(['release_year'])
df_year_genre = df_year_genre.sort_values('release_year')
#print(df_year_genre)

# Visualize which the year and most popular corresponding genre
plt.scatter(df_year_genre['release_year'], df_year_genre['genres'])
plt.xticks(df_year_genre['release_year'])
plt.xticks(rotation=45)
plt.show()

# Remove index from dataframe
df_year_genre = df_year_genre.iloc[:,0:3]
df_year_genre.set_index(['release_year'], inplace=True)
print(df_year_genre)

df_year_genre.to_csv(r'C:\Users\Fotis\Desktop\Udacity\Data Analyst\Introduction to data analysis\Data Analyst project 1\popular_genre_by_year.csv')


