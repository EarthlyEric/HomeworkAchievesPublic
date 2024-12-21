import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


dataset = pd.read_csv('spotify_tracks.csv')

Columns = ['track_name', 'artist_name', 'year', 'popularity',
 'album_name', 'acousticness', 'danceability', 'duration_ms', 'energy',
 'instrumentalness', 'key', 'liveness', 'loudness', 'mode', 'speechiness',
 'tempo', 'time_signature', 'valence', 'language']

if dataset.isnull().values.any():
    print("There are missing values in the dataset")