import os
import time
import pandas as pd

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class SpotifyApiExtractor:

    def __init__(self, se=None):
        '''
        Extractor class
        Input: preprocessor class dataset extracted from spotify API
        '''
        # credentials need to be exported via the command line
        self.auth_manager = SpotifyClientCredentials()

        self.sp_connection = spotipy.Spotify(auth_manager=self.auth_manager)
        self.search_limit = 10
        self.se = se


    def get_track_base_attrs(self, title, artist):
        '''
        Function that returns the basic features of a desired song
        if it's not present in the local dataset
        '''
        self.ta_response = self.sp_connection.search(
            q="artist:" + artist + " track:" + title,
            type="track",
            limit=1)
        #print(self.ta_response)

        # parse attributes from track
        if len(self.ta_response['tracks']['items']) == 0:
            return None
        else:
            self.track = self.ta_response['tracks']['items'][0]

        self.track_id = self.track['id']
        self.track_name = self.track['name']
        self.track_uri = self.track['uri']
        self.track_popularity = self.track['popularity']
        self.track_explicit = self.track['explicit']
        self.track_artists = [artist['name'] for artist in self.track['artists']]

        # get track features
        self.track_features = self.sp_connection.audio_features(tracks = self.track_uri)[0]

        return [self.track_name, self.track_artists, self.track_id,
                self.track_features['danceability'], self.track_features['energy'],
                self.track_features['valence'], self.track_features['tempo']]


    def get_tracks_and_artists(self, titles, artists):

        songs_attrs = []

        for title, artist in zip(titles, artists):

            attrs = self.get_track_base_attrs(title, artist)

            if attrs is not None:
                songs_attrs.append(attrs)

        #time.sleep(1)

        return pd.DataFrame(songs_attrs, columns=['Track', 'Artists', 'ID', 'Danceability', 'Energy', 'Valence', 'Tempo'])
