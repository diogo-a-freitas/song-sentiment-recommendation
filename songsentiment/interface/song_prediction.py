
from songsentiment.user_topics import pre_process_user_input

from songsentiment.musixmatch_function import search_lyrics

from songsentiment.lyric_sentiment import adding_sentiment_columns


def predict_songs(text_user: str):

    top_words_list = pre_process_user_input(text_user)

    return top_words_list

def musixmatch(top_words_list):

    new_lyrics_df, list_of_artists, list_of_tracks = search_lyrics(top_words_list)

    return new_lyrics_df, list_of_artists, list_of_tracks

def clean_lyrics(new_lyrics_df):

    cleaned_lyrics_df = adding_sentiment_columns(new_lyrics_df)
    return cleaned_lyrics_df
