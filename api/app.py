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


if len(utext) < 20:
        st.markdown('Please input more than 20 characters')

elif len(utext) > 140:
        st.markdown('Please input less than 140 characters')

else:
        '''---'''

        res = requests.get(url, params).json()

        st.markdown('Sentiment: *' + str(res['user_sentiment']['label']) +
                        '* with a score of ' + str(round(res['user_sentiment']['score'], 2)))

        st.markdown('Topics: ' + ', '.join(res['user_topics']))

        """
        ---
        Our recommendation for you:
        """

        for song in res['songs']:

            if res['user_sentiment']['label'] == song['sentiment_label']:

                url = f"https://open.spotify.com/embed/track/{song['id']}?utm_source=generator"

                components.iframe(url, height=80)

                st.markdown('Song cluster: '   + str(song['cluster']))
                st.markdown('Song valence: '   + str(round(song['valence'], 2)))
                st.markdown('Song sentiment: ' + str(song['sentiment_label']))
                st.markdown('Song sentiment score: ' + str(round(song['sentiment_score'], 2)))

            elif res['user_sentiment']['label'] == song['sentiment_label']:
                pass

            else:
                pass
