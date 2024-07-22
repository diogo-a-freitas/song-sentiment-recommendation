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
    ---Our recommendation for you:
    """
    #res["songs"] = res["songs"].sort_values(by="valence", ascending=False)
    for song in res['songs']:

        if res['user_sentiment']['label'] == song['sentiment_label']: #and song["cluster"] == 0:

            url = f"https://open.spotify.com/embed/track/{song['id']}?utm_source=generator"

            components.iframe(url, height=80)

            st.markdown('Song cluster: ' + str(song['cluster']))
            st.markdown('Song valence: ' + str(song['valence']))
            st.markdown('Song Sentiment Score: ' + str(song['sentiment_score']))
            st.markdown('Song Sentiment Score: ' + str(song['sentiment_label']))

        #elif res['user_sentiment']['label'] == song['sentiment_label']:
            #pass

        else:
            pass
