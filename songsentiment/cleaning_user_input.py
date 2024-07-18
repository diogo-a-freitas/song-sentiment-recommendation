#clean user input and remove stop words

import re
import string
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import nltk
from textblob import TextBlob
import unicodedata
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')


def preprocessing(sentence):

    #correct grammar
    blob = TextBlob(sentence)
    sentence = str(blob.correct())

    #remove white spaces
    sentence = sentence.strip()

    #lower the characters
    sentence = sentence.lower()

    #remove unique characters
    sentence = sentence.replace('½', 'half')

    #remove numbers
    sentence = re.sub(r'\b\d+\b', '', sentence)

    # Normalize the text to remove accents and normalize forms
    sentence = unicodedata.normalize('NFD', sentence).encode('ascii', 'ignore').decode('utf-8')

    # Remove remaining non-ASCII characters
    sentence = re.sub(r'[^\x00-\x7F]+', ' ', sentence)

    #remove emails
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    sentence = re.sub(email_pattern, '', sentence)

    #remove twitter handles
    handle_pattern = r'@\w+'
    sentence = re.sub(handle_pattern, '', sentence)

    #remove twitter emoticons
    emoticon_pattern = r'[:;=8][\-o\*\']?[\)\]\(\[dDpP/:}{@|\\]'
    sentence = re.sub(emoticon_pattern, '', sentence)

    #remove websites
    url_pattern = r'https?://\S+|www\.\S+'
    sentence = re.sub(url_pattern, '', sentence)

    #remove numbers
    sentence = ''.join(char for char in sentence if not char.isdigit())

    #tokenize sentence
    tokens = word_tokenize(sentence)

    #remove stop words
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]

    # Remove punctuation
    filtered_tokens = [''.join([c for c in word if c not in string.punctuation]) for word in filtered_tokens if word not in string.punctuation]

    #repeated characters
    pattern = re.compile(r"(.)\1{2,}")
    filtered_tokens = [pattern.sub(r"\1", word) for word in filtered_tokens]

    #lemmatize the tokens
    wnl = WordNetLemmatizer()
    #iterate with lemmatizer for verbs
    verb_lemmatize_words = [wnl.lemmatize(word, pos = "v") for word in filtered_tokens]
    #iterate with lemmatizer for nouns
    noun_lemmatize_words = [wnl.lemmatize(word, pos = "n") for word in verb_lemmatize_words]

    #join tokens
    sentence = ' '.join(noun_lemmatize_words)
    return sentence
