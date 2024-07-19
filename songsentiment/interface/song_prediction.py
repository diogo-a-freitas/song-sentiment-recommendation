
from songsentiment.user_topics import pre_process_user_input

from songsentiment.musixmatch_function import search_lyrics

from songsentiment.lyric_sentiment import adding_sentiment_columns

from songsentiment.spotify_track import SpotifyApiExtractor

from songsentiment.song_clusters import cluster_prediction


"""def predict_songs(text_user: str):

    top_words_list = pre_process_user_input(text_user)

    return top_words_list

def musixmatch(top_words_list):

    new_lyrics_df = search_lyrics(top_words_list)

    return new_lyrics_df

def clean_lyrics(new_lyrics_df):

    cleaned_lyrics_df = adding_sentiment_columns(new_lyrics_df)
    return cleaned_lyrics_df

#print(clean_lyrics(musixmatch(['know', 'morning', 'better', 'good', 'good morning'])[0]))


list_spotify_artists = clean_lyrics(musixmatch(['know', 'morning', 'better', 'good', 'good morning']))['Artist']

list_spotify_tracks = clean_lyrics(musixmatch(['know', 'morning', 'better', 'good', 'good morning']))['Track']

def spotify_features(list_of_tracks, list_of_artists):

    spotify_extractor = SpotifyApiExtractor()

    songs_df = spotify_extractor.get_tracks_and_artists(list_of_tracks, list_of_artists)

    return songs_df"""

#print(spotify_features(list_spotify_tracks, list_spotify_artists))

spotify_features = SpotifyApiExtractor().get_tracks_and_artists(['Gasoline', 'Espresso'], ['The Weeknd', 'Sabrina Carpenter'])
X = spotify_features.select_dtypes(exclude='object')

def kmeans(spotify_data):

    #spotify_features = SpotifyApiExtractor().get_tracks_and_artists(['Gasoline', 'Espresso'], ['The Weeknd', 'Sabrina Carpenter'])

    spotify_features['cluster'] = cluster_prediction(spotify_data)

    return spotify_features

print(kmeans(X))
