import streamlit as st
import requests

import streamlit.components.v1 as components

'''
# Song sentiment recommendation
'''

st.markdown('''Let's see how you are feeling today and recommend a song for you!''')

utext  = st.text_input('How are you and what comes in your mind:', '')

url = 'http://127.0.0.1:8000/predict'

params = dict(
    text = utext
)


if len(utext) < 70:

        st.markdown('Please input more than 70 characters')

elif len(utext) > 140:
        st.markdown('Please input less than 140 characters')

else:

        '''---'''

        res = requests.get(url, params).json()

        st.markdown('Sentiment: *' + str(res['user_sentiment']['label']) +
                        '* with a score of ' + str(round(res['user_sentiment']['score'], 2)))

        st.markdown('Topics: ' + ', '.join(res['user_topics']))

        for song in res['songs']:

            if res['user_sentiment']['label'] == song['sentiment_label']:


                url = f"https://open.spotify.com/embed/track/{song['id']}?utm_source=generator"

                components.iframe(url, height=80)

                st.markdown('Song cluster: ' + str(song['cluster']))
                st.markdown('Song valence: ' + str(song['valence']))
                st.markdown('Song Sentiment Score: ' + str(song['sentiment_score']))
                st.markdown('Song Sentiment Score: ' + str(song['sentiment_label']))#

            elif res['user_sentiment']['label'] == song['sentiment_label']:











        #st.markdown('Sentiment: *' + str(res['user_sentiment']['label']) +
                 #   '* with a score of ' + str(round(res['user_sentiment']['score'], 2)))

        #st.markdown('Topics: ' + ', '.join(res['user_topics']))

        #"""
        #---
        #Our recommendation for you:
        #"""

        #for song in res['songs']:
            #url = f"https://open.spotify.com/embed/track/{song['id']}?utm_source=generator"

            #components.iframe(url, height=80)
            #st.markdown('Song cluster: ' + str(song['cluster']))
            #st.markdown('Song valence: ' + str(song['valence']))
            #st.markdown('Song Sentiment Score: ' + str(song['sentiment_score']))
            #st.markdown('Song Sentiment Score: ' + str(song['sentiment_label']))

# surl1 = "https://open.spotify.com/embed/track/6Y4rniIxibegzsg8cdWAWV?utm_source=generator"
# surl2 = "https://open.spotify.com/embed/track/2Uf9WTBWMA8S9Lh3k3Rui6?si=7dfd2575e59e4264?utm_source=generator"

# components.iframe(url, height=80)
# components.iframe(surl2, height=80)
