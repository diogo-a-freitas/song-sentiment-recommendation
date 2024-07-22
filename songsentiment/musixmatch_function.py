from songsentiment.user_topics import pre_process_user_input
import requests
import os
import pandas as pd

#

#function to get songs
def search_lyrics(top_words):

    #create lists of song details
    list_of_artists = []
    list_of_tracks = []
    list_of_track_ids = []
    list_of_lyrics = []
    list_of_artist_id = []
    list_of_album_names = []

    url = 'https://api.musixmatch.com/ws/1.1/track.search'

    api_key= os.environ.get('MUSIXMATCH')

    params = {'apikey': api_key,
         'q_lyrics': f"{top_words}",
         'f_has_lyrics': True,
         's_track_rating': 'desc',
         'quorum_factor': 0.9}
         #'page_size': 50}


    response = requests.get(url, params=params).json()


    index = 0
    while index < len(response['message']['body']['track_list']):

        #get gate to song details
        base_response = response['message']['body']['track_list'][index]

        #get song details
        artist_name = base_response['track']['artist_name']
        track_name = base_response['track']['track_name']
        track_id = base_response['track']['track_id']
        artist_id = base_response['track']['artist_id']
        album_name = base_response['track']['album_name']
        list_of_artists.append(artist_name)
        list_of_tracks.append(track_name)
        list_of_track_ids.append(track_id)
        list_of_artist_id.append(artist_id)
        list_of_album_names.append(album_name)

        #connect to lyrics endpoint
        url_lyrics = 'https://api.musixmatch.com/ws/1.1/track.lyrics.get'
        params_lyrics = {'apikey': api_key, 'track_id': track_id}
        lyrics_response = requests.get(url_lyrics, params=params_lyrics).json()
        lyrics_snippet = lyrics_response['message']['body']['lyrics']['lyrics_body']
        list_of_lyrics.append(lyrics_snippet)
        index += 1

    #turn in dataframe
    new_lyrics_df = pd.DataFrame({
                        'Artist_id': list_of_artist_id,
                        'Artist': list_of_artists,
                        'Track': list_of_tracks,
                        'Track_ID': list_of_track_ids,
                        'Album_Name': list_of_album_names,
                        'Lyric_Snippet': list_of_lyrics})

    return new_lyrics_df
