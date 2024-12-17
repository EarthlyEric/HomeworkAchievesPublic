import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Removed unused columns and saved the cleaned dataset to a new CSV file.
# Check for missing values.

dataset = pd.read_csv('spotify_tracks.csv')

useColumns = ['track_name', 'artist_name', 'year', 'popularity',
 'album_name', 'acousticness', 'danceability', 'duration_ms', 'energy',
 'instrumentalness', 'key', 'liveness', 'loudness', 'mode', 'speechiness',
 'tempo', 'time_signature', 'valence', 'language']

dataset = dataset[useColumns]

dataset.to_csv('spotify_tracks_cleaned.csv', index=False)

newDataset = pd.read_csv('spotify_tracks_cleaned.csv')

if newDataset.isnull().values.any():
    print("There are missing values in the dataset")