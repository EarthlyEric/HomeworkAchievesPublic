import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('spotify_tracks.csv')
average = {}

useColumns = ['danceability', 'acousticness', 'duration_ms', 'energy', 'instrumentalness', 'key', 'liveness', 'loudness', 'mode', 'speechiness', 'tempo', 'valence']
for column in useColumns:
    average[column] = np.mean(dataset[column])
print("平均適合跳舞程度: ", average['danceability'])
print("平均聲學性: ", average['acousticness'])
print("平均歌曲時長: ",  f"{int(average['duration_ms'] / 1000 // 60)} 分 {int(average['duration_ms'] / 1000 % 60)} 秒")
print("平均能量: ", average['energy'])
print("平均演奏性: ", average['instrumentalness'])
print("平均音調: ", average['key'])
print("平均現場感: ", average['liveness'])
print("平均響度: ", average['loudness'], "dB")
print("平均調性模式: ", average['mode'])
print("平均語音性: ", average['speechiness'])
print("平均節奏: ", average['tempo'], "bpm")
print("平均情感: ", average['valence'])