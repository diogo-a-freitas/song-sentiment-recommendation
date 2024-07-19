import pandas as pd
import pickle

def cluster_prediction(X):
    with open('/Users/diogofreitas/code/diogo-a-freitas/song-sentiment-recommendation/model_small/pipeline_spotify.pkl', 'rb') as file:
        model = pickle.load(file)

    return model.predict(X)
