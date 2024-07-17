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

if utext:

    '''---'''

    res = requests.get(url, params).json()

    st.markdown('Sentiment: *' + str(res['sentiment']) + '* with a score of ' + str(round(res['score'], 2)))

    surl1 = "https://open.spotify.com/embed/track/6Y4rniIxibegzsg8cdWAWV?utm_source=generator"
    surl2 = "https://open.spotify.com/embed/track/2Uf9WTBWMA8S9Lh3k3Rui6?si=7dfd2575e59e4264?utm_source=generator"

    """
    ---
    Our recommendation for you:
    """

    components.iframe(surl1, height=100)
    components.iframe(surl2, height=100)
