import pandas as pd
import pickle

def cluster_prediction(X):
    with open('model_small/pipeline_spotify.pkl', 'rb') as file:
        model = pickle.load(file)

    return model.predict(X)
