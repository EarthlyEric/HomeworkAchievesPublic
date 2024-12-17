import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

cleanedDataset = pd.read_csv('spotify_tracks_cleaned.csv')

yearReleased = cleanedDataset['year']

Bar = plt.bar(yearReleased.value_counts().index, yearReleased.value_counts().values, color='skyblue')
plt.xlabel('Release Year')
plt.ylabel('Number of Songs')
plt.title('Number of Songs Released on Spotify Every Year')
plt.savefig(os.path.join('output','Number of Songs Released on Spotify Every Year.png'))
plt.show()