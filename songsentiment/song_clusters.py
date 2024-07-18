import pandas as pd
import pickle

with open('model_small/spotify_pca.pkl', 'rb') as pickle_file:
    spotify_pca = pickle.load(pickle_file)
print(spotify_pca)
