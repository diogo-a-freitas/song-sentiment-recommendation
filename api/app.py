import streamlit as st
import requests

import streamlit.components.v1 as components


verbosity = 2

#Set Header Config (name on tab)
st.set_page_config(
    page_title="MoodTracks",
    page_icon="🎶",
)

with open("api/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

#Set Title
st.markdown("<h1 style='text-align: center;'>🎶 MoodTracks</h1>", unsafe_allow_html=True)

#Set intro marker
st.markdown('''We would love to know how your day is going so far! Please tell us all about it, we won't tell a soul! 🤫''')


#store sentiment info between forms
if 'sentiment_label' not in st.session_state:
    st.session_state.sentiment_label = None
    st.session_state.sentiment_score = None
    st.session_state.user_topics = None
    st.session_state.songs = []
    st.session_state.submitted = None

#instantiate form
with st.form("my_form"):

    utext  = st.text_area(max_chars=140, placeholder='Please write your massage here', label='form', height=10, label_visibility='hidden')
    st.caption('Please write a message above 50 and below 140 characters')

    options = st.radio(
                        "Listen to songs that:",
                        [
                            "match the topics we discovered and your mood?",
                            "match the topics we discovered and improve your mood?",
                            "don't match the topics we discovered and improve your mood?"
                        ],
                        index=None,
                    )
    submitted = st.form_submit_button("Submit")

    if submitted:

        if len(utext) == 0 and options == None:

            st.warning('Please write a message in the text box and select one of the options above', icon="⚠️")

        elif (len(utext) < 20 and len(utext) != 0) or options == None:
            st.warning('Please input more than 20 characters and select one of the options above', icon="⚠️")

        else:

            reverse_value = True

            params = dict(text = utext, reverse_order=reverse_value)

            reverse_value = True

            url = 'http://127.0.0.1:8000/predict'
            params = dict(text = utext, reverse_order=True)
            res = requests.get(url, params).json()

            st.session_state.sentiment_label = res['user_sentiment']['label']
            st.session_state.sentiment_score = round(res['user_sentiment']['score'], 2)
            st.session_state.user_topics = res['user_topics']

            sentiment_label = st.session_state.sentiment_label
            sentiment_score = st.session_state.sentiment_score
            sentiment_map = {'2': 'negative', '1': 'neutral', '0': 'positive'}
            sentiment_int = sentiment_map.get(sentiment_label, -1)

            #logic on messages for final user
            if sentiment_label == 'positive':
                color_classes = ['thermometer-red', 'thermometer-yellow', 'thermometer-green']
                emoji_classes = ['emoji-green', 'emoji-yellow', 'emoji-red']
                emojis = ['😔', '😶', '😂']
                emoji_styles = [
                    "display: none;",  # For 'negative'
                    "display: none;",  # For 'neutral'
                    "display: block;"  # For 'positive'
                ]
            elif sentiment_label == 'neutral':
                color_classes = ['thermometer-red', 'thermometer-yellow', 'thermometer-green']
                emoji_classes = ['emoji-yellow', 'emoji-green', 'emoji-red']
                emojis = ['😔', '😶', '😂']
                emoji_styles = [
                    "display: none;",  # For 'negative'
                    "display: block;",  # For 'neutral'
                    "display: none;"   # For 'positive'
                ]
            elif sentiment_label == 'negative':
                color_classes = ['thermometer-red', 'thermometer-yellow', 'thermometer-green']
                emoji_classes = ['emoji-red', 'emoji-yellow', 'emoji-green']
                emojis = ['😔', '😶', '😂']
                emoji_styles = [
                    "display: block;",  # For 'negative'
                    "display: none;",   # For 'neutral'
                    "display: none;"    # For 'positive'
                ]
            else:
                # Default case (in case of unexpected value)
                color_classes = ['thermometer-red', 'thermometer-yellow', 'thermometer-green']
                emoji_classes = ['emoji-yellow', 'emoji-green', 'emoji-red']
                emojis = ['😔', '😶', '😂']
                emoji_styles = [
                    "display: none;",
                    "display: none;",
                    "display: none;"
                ]

            # Display the thermometer with emojis
            st.markdown(f"""
                <style>
                    @import url('api/styles.css');
                </style>
                <div class="thermometer-container">
                    <div class="thermometer-section {color_classes[0]}" style="width: 33.33%;">
                        <div class="emoji {emoji_classes[0]}" style="{emoji_styles[0]}">{emojis[0]}</div>
                    </div>
                    <div class="thermometer-section {color_classes[1]}" style="width: 33.33%;">
                        <div class="emoji {emoji_classes[1]}" style="{emoji_styles[1]}">{emojis[1]}</div>
                    </div>
                    <div class="thermometer-section {color_classes[2]}" style="width: 33.34%;">
                        <div class="emoji {emoji_classes[2]}" style="{emoji_styles[2]}">{emojis[2]}</div>
                    </div>
                </div>
                <div class="thermometer-label" style="text-align: center; margin-top: 10px;">{sentiment_label.capitalize()}</div>
            """, unsafe_allow_html=True)

            st.markdown(f'We detected a {sentiment_label} sentiment from your message with a score of {sentiment_score}.')

            #additional info on the meaning of the labels
            if sentiment_int == 0 and verbosity > 0:

                st.markdown(
                            """
                            You may be feeling emotions such as:

                            - Disappointment - :disappointed:
                            - Anger - :angry:
                            - Worry - :worried:
                            - Fear - :cold_sweat:
                            - Tiredness - :tired_face:
                            - Sadness - :pensive:

                            And we are sad to hear that, so we hope our recommendations make you feel better!
                            """
                            )
                st.markdown('''
                            <style>
                            [data-testid="stMarkdownContainer"] ul{
                                padding-left:40px;
                            }
                            </style>
                            ''', unsafe_allow_html=True)

            elif sentiment_int == 1 and verbosity > 0:

                st.markdown(
                            """
                            You may be feeling emotions such as:

                            - Apathetic - :neutral_face:
                            - ?? - :no_mouth:
                            - Emotionless - :expressionless:
                            - Confusion - :confused:
                            - Relief - :relieved:

                            And we hope our recommendations bring a bit more spark to your day :sparkles:
                            """
                            )
                st.markdown('''
                            <style>
                            [data-testid="stMarkdownContainer"] ul{
                                padding-left:40px;
                            }
                            </style>
                            ''', unsafe_allow_html=True)
            elif verbosity > 0:
                st.markdown(
                            """
                            You may be feeling emotions such as:

                            - Joy - :joy:
                            - Satisfaction - :satisfied:
                            - Love - :heart_eyes:
                            - Happiness - :grin:
                            - Euphoric - :partying_face:

                            And we hope our recommendations match your mood!
                            """
                            )
                st.markdown('''
                            <style>
                            [data-testid="stMarkdownContainer"] ul{
                                padding-left:40px;
                            }
                            </style>
                            ''', unsafe_allow_html=True)

            st.markdown("<h1 style='text-align: center;'>🎶 OUR RECOMENDATIONS 🎶</h1>", unsafe_allow_html=True)

            if options == 'that match the topics we discovered and your mood?':

                for song in res['songs']:

                    if res['user_sentiment']['label'] == song['sentiment_label']:

                        url = f"https://open.spotify.com/embed/track/{song['id']}?utm_source=generator"
                        components.iframe(url, height=80)

                        if verbosity > 1:
                            st.markdown('Song cluster: '   + str(song['cluster']))
                            st.markdown('Song valence: '   + str(round(song['valence'], 2)))
                            st.markdown('Song sentiment: ' + str(song['sentiment_label']))
                            st.markdown('Song sentiment score: ' + str(round(song['sentiment_score'], 2)))


            elif options == 'that match the topics we discovered and improve your mood?':

                sorted_songs = sorted(res['songs'], key=lambda x: x['valence'], reverse=True)

                for song in sorted_songs:

                    if res['user_sentiment']['label'] == song['sentiment_label'] and song["cluster"] == 0:

                        url = f"https://open.spotify.com/embed/track/{song['id']}?utm_source=generator"
                        components.iframe(url, height=80)

                        if verbosity > 1:
                            st.markdown('Song cluster: '   + str(song['cluster']))
                            st.markdown('Song valence: '   + str(round(song['valence'], 2)))
                            st.markdown('Song sentiment: ' + str(song['sentiment_label']))
                            st.markdown('Song sentiment score: ' + str(round(song['sentiment_score'], 2)))

            else:
                reverse_value=False

                sorted_songs = sorted(res['songs'], key=lambda x: x['valence'], reverse=True)

                for song in sorted_songs:

                    if res['user_sentiment']['label'] == song['sentiment_label'] and song["cluster"] == 0:

                        url = f"https://open.spotify.com/embed/track/{song['id']}?utm_source=generator"
                        components.iframe(url, height=80)

                        if verbosity > 1:
                            st.markdown('Song cluster: '   + str(song['cluster']))
                            st.markdown('Song valence: '   + str(round(song['valence'], 2)))
                            st.markdown('Song sentiment: ' + str(song['sentiment_label']))
                            st.markdown('Song sentiment score: ' + str(round(song['sentiment_score'], 2)))
