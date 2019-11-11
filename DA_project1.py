import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
desired_width=720
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns',25)

def read_data():
    '''Loads data to a pandas dataframe'''

    df = pd.read_csv('tmdb-movies.csv')
    return df

def miss_values(df):
    '''Checks for missing values in columns required for the analysis and drops rows with NaN values'''

    # Check for missing values in columns popularity, release year and genres
    print(df['genres'].isnull().values.any())
    print(df['release_year'].isnull().values.any())
    print(df['popularity'].isnull().values.any())
    # Drop rows where there is no genre indicated
    df = df.dropna(how='any', subset=['genres'])
    print(df['genres'].isnull().values.any())
    return df

def final_dataframe(df):
    '''Creates a dataframe grouped by release year and genre where the mean popularity is shown.
       Then, for each year, it extracts the most popular genre'''

    # Convert genre column to a list
    df['genres'] = df['genres'].str.split('|')

    # Make a new row for every element in the genre values list
    df = df.explode('genres')

    # Create dataframe with info on the average popularity of each genre each year
    df_year_genre = df.groupby(['release_year','genres'], as_index=False).popularity.mean()
    #print(df_year_genre.head(20))

    # Extract the max average popularity and the genre type for each year
    df_year_genre = df_year_genre.sort_values('popularity', ascending=False).drop_duplicates(['release_year'])
    df_year_genre = df_year_genre.sort_values('release_year')
    #print(df_year_genre)
    return df_year_genre

def visualise(df_year_genre,df):
    ''' Creates a plot where the most popular genre is shown for each year'''

    # Visualize which the year and most popular corresponding genre
    plt.hlines(y=df_year_genre['genres'], xmin=1960, xmax=df_year_genre['release_year'], color='skyblue')
    plt.plot(df_year_genre['release_year'], df_year_genre['genres'], "D")
    plt.xticks(df_year_genre['release_year'], fontsize=9)
    plt.xticks(rotation=45)
    plt.title('Most popular film genre each year', fontsize=20)
    plt.xlabel('Year', fontsize=16)
    plt.ylabel(' Film genre', fontsize=16);

    print(df.corr())
    df.plot(x='revenue', y='popularity', kind='scatter')
    plt.title('Association of revenues over the popularity of movies', fontsize=20)
    df.plot(x='revenue', y='budget', kind='scatter')
    plt.title('Association of revenues over the budget of movies', fontsize=20)
    df.plot(x='revenue', y='vote_count', kind='scatter')
    plt.title('Association of revenues over the nr. of votes ofa movie', fontsize=20)
    plt.show()

    return df_year_genre

def get_table(df_year_genre):
    ''' Creates a table showing the release year and corresponding most popular genre.'''

    # Remove index from dataframe
    df_year_genre = df_year_genre.iloc[:,0:3]
    df_year_genre.set_index(['release_year'], inplace=True)
    print(df_year_genre)
    df_year_genre.to_csv(r'C:\Users\Fotis\Desktop\Udacity\Data Analyst\Introduction to data analysis\Data Analyst project 1\popular_genre_by_year.csv')

def main():
    df = read_data()
    df = miss_values(df)
    df_year_genre = final_dataframe(df)
    df_year_genre = visualise(df_year_genre,df)
    get_table(df_year_genre)
    return df

if __name__ == "__main__":
	df = main()

