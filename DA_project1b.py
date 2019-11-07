import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
desired_width=720
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns',25)


df = pd.read_csv('tmdb-movies.csv')


x = df[df['revenue'] > df['revenue'].mean()]
print(x.describe())