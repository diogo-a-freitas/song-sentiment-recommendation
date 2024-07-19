from songsentiment.user_topics import pre_process_user_input
from songsentiment.musixmatch_function import search_lyrics
from songsentiment.lyric_sentiment import adding_sentiment_columns
from songsentiment.spotify_track import SpotifyApiExtractor
from songsentiment.song_clusters import cluster_prediction

from transformers import pipeline

pipe = pipeline(model= "cardiffnlp/twitter-roberta-base-sentiment-latest")


def get_user_sentiment(text: str):
    return pipe(text)[0]


def predict_songs(text_user: str):

    top_words_list = pre_process_user_input(text_user)
    return top_words_list


def musixmatch(top_words_list):

    new_lyrics_df = search_lyrics(top_words_list)
    return new_lyrics_df


def clean_lyrics(new_lyrics_df):

    cleaned_lyrics_df = adding_sentiment_columns(new_lyrics_df)
    return cleaned_lyrics_df


def spotify_features(list_tracks, list_artists):

    spotify = SpotifyApiExtractor()

    songs_df = spotify.get_tracks_and_artists(list_tracks, list_artists)
    return songs_df

mmatch = musixmatch(['know', 'morning', 'better', 'good', 'good morning'])

list_tracks  = clean_lyrics(mmatch)['Track']
list_artists = clean_lyrics(mmatch)['Artist']

print(spotify_features(list_tracks, list_artists))


#spotify_features = SpotifyApiExtractor().get_tracks_and_artists(['Gasoline', 'Espresso'], ['The Weeknd', 'Sabrina Carpenter'])
#X = spotify_features.select_dtypes(exclude='object')

def kmeans(spotify_data):

    #spotify_features = SpotifyApiExtractor().get_tracks_and_artists(['Gasoline', 'Espresso'], ['The Weeknd', 'Sabrina Carpenter'])

    spotify_features['cluster'] = cluster_prediction(spotify_data)

    return spotify_features

#print(kmeans(X))
