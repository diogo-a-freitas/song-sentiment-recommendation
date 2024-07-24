from songsentiment.user_topics import pre_process_user_input

import requests
import os
import pandas as pd

#import feather package and numpy

import pyarrow.feather as feather
import pandas as pd
import random

# Load feather file
first_million_clean_tags = feather.read_feather('raw_data/first_million_clean_tags_02.feather')

def search_lyrics(top_words):

    #create lists of song details
    list_of_artists = []
    list_of_tracks = []
    list_of_lyrics = []

    #get a random sample of 500 songs:
    random_sample = first_million_clean_tags.sample(n=500)

    def any_top_word_in_tags(tags, top_words):
        return any(word in tags for word in top_words)


    filtered_data = random_sample[random_sample['tags'].apply(lambda tags: any_top_word_in_tags(tags, top_words))]


    list_of_artists = filtered_data['artist'].tolist()
    list_of_tracks = filtered_data['title'].tolist()
    list_of_lyrics = filtered_data['clean_text'].tolist()

    #turn in dataframe
    new_lyrics_df = pd.DataFrame({
                        'Artist': list_of_artists,
                        'Track': list_of_tracks,
                        'Lyric_Snippet': list_of_lyrics})

    return new_lyrics_df[0:10]

print(search_lyrics(['im', 'mean', 'kill', 'science', 'today']))
