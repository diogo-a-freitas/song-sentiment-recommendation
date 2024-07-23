from songsentiment.user_topics import pre_process_user_input
from songsentiment.musixmatch_function import search_lyrics
from songsentiment.lyric_sentiment import adding_sentiment_columns
from songsentiment.spotify_track import SpotifyApiExtractor
from songsentiment.song_clusters import cluster_prediction

import pandas as pd

from transformers import pipeline

pipe = pipeline(model= "cardiffnlp/twitter-roberta-base-sentiment-latest")


def get_user_sentiment(text_user: str):
    return pipe(text_user)[0]


def predict_topics(text_user: str, reverse_order: bool):

    top_words_list = pre_process_user_input(text_user, reverse_order)
    return top_words_list


def musixmatch(top_words_list):

    new_lyrics_df = search_lyrics(top_words_list)
    return new_lyrics_df


def clean_lyrics(new_lyrics_df):

    cleaned_lyrics_df = adding_sentiment_columns(new_lyrics_df)
    return cleaned_lyrics_df


def spotify_features(list_tracks, list_artists, list_slabel, list_sscore):

    spotify = SpotifyApiExtractor()

    songs_df = spotify.get_tracks_and_artists(list_tracks, list_artists, list_slabel, list_sscore)
    return songs_df

#mmatch = musixmatch(['know', 'morning', 'better', 'good', 'good morning'])
#list_tracks  = clean_lyrics(mmatch)['Track']
#list_artists = clean_lyrics(mmatch)['Artist']
#print(spotify_features(list_tracks, list_artists))


def kmeans(spotify_data):

    X = spotify_data.select_dtypes(exclude='object')
    X = X.drop(columns=['sentiment_score'])

    spotify_data['cluster'] = cluster_prediction(X)

    return spotify_data

#spotify_features = spotify_features(list_tracks, list_artists)
#X = spotify_features.select_dtypes(exclude='object')
#print(kmeans(X))


def predict_songs(text: str, reverse_order: bool):

    user_sent = get_user_sentiment(text)
    top_words_list = predict_topics(text, reverse_order)

    mmatch = musixmatch(top_words_list)
    cleaned_lyrics = clean_lyrics(mmatch)

    list_tracks  = cleaned_lyrics['Track']
    list_artists = cleaned_lyrics['Artist']

    list_slabel = cleaned_lyrics['sentiment_label']
    list_sscore = cleaned_lyrics['sentiment_score']

    songs_df = spotify_features(list_tracks, list_artists, list_slabel, list_sscore)

    final_df = kmeans(songs_df)

    return (final_df, user_sent, top_words_list)

#print(predict_songs("This data frame is great", True))
