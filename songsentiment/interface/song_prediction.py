from songsentiment.user_topics import pre_process_user_input
from songsentiment.musixmatch_function import search_lyrics
from songsentiment.lyric_sentiment import adding_sentiment_columns
from songsentiment.spotify_track import SpotifyApiExtractor


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

    songs_df = spotify.get_tracks_and_artists(list(list_tracks), list(list_artists))
    return songs_df


mmatch = musixmatch(['know', 'morning', 'better', 'good', 'good morning'])

list_tracks  = clean_lyrics(mmatch)['Track']
list_artists = clean_lyrics(mmatch)['Artist']

print(spotify_features(list_tracks, list_artists))
