# Imports
import pandas as pd
import re
import string
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import requests
from transformers import pipeline
from musixmatch import search_lyrics

def clean_lyrics(text):
    """Cleans lyrics from MusicMatchAPI"""
    text = text.replace("\n", " ")  # Replace newline characters with space
    text = re.sub(r'\[.*?\]', '', text)  # Remove text within brackets and the brackets
    text = text.replace("\'", "") # Removes Slashes
    text = text.strip() # Removes uneccesary whitespaces
    text = text.lower() # Lowers
    text = ''.join(char for char in text if not char.isdigit()) # Removes digits
    for punctuation in string.punctuation:
        text = text.replace(punctuation, '') # Removes punctuation
    return text

def tokenize(text):
    """Tokenizes the lyrics"""
    text_tk = word_tokenize(text)
    return text_tk

def lemmatize(tokenized_text):
    """Lemmatizes the lyrics"""
    # lemmatizing the verbs and nouns
    verb_lemmatized = [WordNetLemmatizer().lemmatize(word, pos = "v") for word in tokenized_text]
    noun_lemmatized = [WordNetLemmatizer().lemmatize(word, pos = "n") for word in verb_lemmatized]
    #joining lemmatized lyrics to string
    lemmatized_lyrics = " ".join(noun_lemmatized)
    return lemmatized_lyrics

def preprocessing(text):
    """Combining the previous steps"""
    text = clean_lyrics(text)
    text = tokenize(text)
    text = lemmatize(text)
    return text

def get_sentiment_score(text):
    """Gets the sentiment score"""
    pipe = pipeline("text-classification", model="cardiffnlp/twitter-roberta-base-sentiment-latest")
    result = pipe(text[:514])[0]
    return result['score']

def get_sentiment_label(text):
    """Gets the sentiment label"""
    pipe = pipeline("text-classification", model="cardiffnlp/twitter-roberta-base-sentiment-latest")
    result = pipe(text[:514])[0]
    return result['label']


def adding_sentiment_columns(new_lyrics_df):
    """Applying lyric sentiment to each song"""
    new_lyrics_df['cleaned_lyrics'] = new_lyrics_df['Lyric_Snippet'].apply(preprocessing)
    new_lyrics_df["sentiment_score"] = new_lyrics_df["cleaned_lyrics"].apply(get_sentiment_score)
    new_lyrics_df["sentiment_label"] = new_lyrics_df["cleaned_lyrics"].apply(get_sentiment_label)
    return new_lyrics_df

if __name__ == "__main__":
    # Example query
    query = "hello from the other side"
    new_lyrics_df = search_lyrics(query)
    new_lyrics_df = adding_sentiment_columns(new_lyrics_df)
    print(new_lyrics_df)
