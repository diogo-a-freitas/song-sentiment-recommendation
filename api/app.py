import streamlit as st
import requests

import streamlit.components.v1 as components


#Set Header Config (name on tab)
st.set_page_config(
    page_title="MoodTrack",
    page_icon="🎶",
)

#Set Title
st.markdown("<h1 style='text-align: center; color: white;'>🎶MoodTrack</h1>", unsafe_allow_html=True)

#Set intro marker
st.markdown('''We would love to know how your day is going so far! Please tell us all about it, we won't tell a soul! 🤫''')

#Input text box
utext  = st.text_area(max_chars=140, placeholder='Please write your massage here', label='', height=10)

st.caption('Please write us a message above 50 and below 140 characters')

with open("api/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)




if len(utext) == 0:
    pass


elif len(utext) < 20 and len(utext) != 0:
        st.markdown("<p1 style='text-align: center; color: #a83250;'><b>Please input <em>more</em> than 20 characters</b></p1>", unsafe_allow_html=True)

#elif len(utext) > 140:
        #st.markdown('Please input less than 140 characters')

else:

    """



    """

    #make request to api
    url = 'http://127.0.0.1:8000/predict'
    params = dict(text = utext)
    res = requests.get(url, params).json()

    #Call User Sentiment Atributes

    sentiment_label = res['user_sentiment']['label']

    sentiment_score = round(res['user_sentiment']['score'], 2)

    sentiment_map = {'negative': 0, 'neutral': 1, 'positive': 2}

    sentiment_int = sentiment_map.get(sentiment_label)


    #if sentiment is negative:
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
    """



    """
    st.markdown(f'We detected a {sentiment_label} sentiment from your message with a score of {sentiment_score}.')


    if sentiment_int == 0:


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

    elif sentiment_int == 1:

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
    else:
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


    # Define options
    options = st.radio(
        "Before we make our recommendations, would you like to:",\
        ["Listen to songs that match the topics we discovered from your message and your mood?", \
            "Listen to songs that match the topics we discovered from your message and improve your mood?", \
                "Listen to songs that don't match the topics we discovered from your message and improve your mood?"])














    #else:
        #pass

        #st.markdown('Topics: ' + ', '.join(res['user_topics']))

    """
    ---
    Our recommendation for you:
    """

    """for song in res['songs']:

        if res['user_sentiment']['label'] == song['sentiment_label']:

            url = f"https://open.spotify.com/embed/track/{song['id']}?utm_source=generator"

            components.iframe(url, height=80)

            st.markdown('Song cluster: ' + str(song['cluster']))
            st.markdown('Song valence: ' + str(song['valence']))
            st.markdown('Song Sentiment Score: ' + str(song['sentiment_score']))
            st.markdown('Song Sentiment Score: ' + str(song['sentiment_label']))

        elif res['user_sentiment']['label'] == song['sentiment_label']:
            pass

        else:
            pass"""
