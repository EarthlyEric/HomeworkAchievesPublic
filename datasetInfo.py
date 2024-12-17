import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dataset = pd.read_csv('spotify_tracks.csv')

print(dataset.columns.values)

"""
Output:
['track_id' 'track_name' 'artist_name' 'year' 'popularity' 'artwork_url'
 'album_name' 'acousticness' 'danceability' 'duration_ms' 'energy'
 'instrumentalness' 'key' 'liveness' 'loudness' 'mode' 'speechiness'
 'tempo' 'time_signature' 'valence' 'track_url' 'language']
"""

print(len(dataset['track_id']))

"""
Output:
62317
"""
if dataset.isnull().values.any():
    print("There are missing values in the dataset")
    
"""
Output:
None
"""




