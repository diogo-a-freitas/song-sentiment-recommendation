import pandas as pd
import numpy as np

import re
import string

from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from transformers import pipeline
from songsentiment.song_lyrics import search_lyrics


def join_lyrics(text):

    if isinstance(text, np.ndarray):

        list_of_strings = text.astype(str).tolist()

        return ' '.join(list_of_strings)

    return ''


pipe = pipeline("text-classification", model="cardiffnlp/twitter-roberta-base-sentiment-latest")


def get_sentiment_score(text):
    """Gets the sentiment score"""
    result = pipe(text[:514])[0]
    return result['score']

def get_sentiment_label(text):
    """Gets the sentiment label"""
    result = pipe(text[:514])[0]
    return result['label']


def adding_sentiment_columns(new_lyrics_df):
    """Applying lyric sentiment to each song"""
    new_lyrics_df['cleaned_lyrics'] = new_lyrics_df['Lyric_Snippet'].apply(join_lyrics)
    new_lyrics_df["sentiment_score"] = new_lyrics_df["cleaned_lyrics"].apply(get_sentiment_score)
    new_lyrics_df["sentiment_label"] = new_lyrics_df["cleaned_lyrics"].apply(get_sentiment_label)
    return new_lyrics_df

#print(adding_sentiment_columns())
