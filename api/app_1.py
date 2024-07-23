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
    sorted_songs = sorted(res['songs'], key=lambda x: x['valence'])

    for song in sorted_songs:

        if res['user_sentiment']['label'] == song['sentiment_label'] and song["cluster"] == 0:

            url = f"https://open.spotify.com/embed/track/{song['id']}?utm_source=generator"

            components.iframe(url, height=80)

            st.markdown('Song cluster: '   + str(song['cluster']))
            st.markdown('Song valence: '   + str(round(song['valence'], 2)))
            st.markdown('Song sentiment: ' + str(song['sentiment_label']))
            st.markdown('Song sentiment score: ' + str(round(song['sentiment_score'], 2)))

        else:
            pass
#Draft for 3rd iteration to replace the one up top to be placed after line25
# model 1

#some elif statement for when checkboxes are there
#'''---'''

#    res = requests.get(url, params).json()
#
#    st.markdown('Sentiment: *' + str(res['user_sentiment']['label']) +
#                        '* with a score of ' + str(round(res['user_sentiment']['score'], 2)))
#
#    st.markdown('Topics: ' + ', '.join(res['user_topics']))
#
#    """
#    ---Our recommendation for you:
#    """
#    for song in res["songs"]:
#       if res["songs"]["cluster"] == 0:
#           song["cluster_label"] = "positive"
#       elif res["songs"]["cluster"] == 1:
#           song["cluster_label"] = "negative"
#       elif res["songs"]["cluster"] == 2:
#           song["cluster_label"] == "neutral"

#    for song in res["songs"]:
#
#        if res['user_sentiment']['label'] == song['sentiment_label'] == song["cluster_label"]:
#
#            url = f"https://open.spotify.com/embed/track/{song['id']}?utm_source=generator"
#
#            components.iframe(url, height=80)
#
#            st.markdown('Song cluster: '   + str(song['cluster']))
#            st.markdown('Song valence: '   + str(round(song['valence'], 2)))
#            st.markdown('Song sentiment: ' + str(song['sentiment_label']))
#            st.markdown('Song sentiment score: ' + str(round(song['sentiment_score'], 2)))

# some elif statement for checkbox
# 2nd model is currently active

# some elif stamtent for checkbox
#3rd model
#'''---'''

#    res = requests.get(url, params).json()
#
#    st.markdown('Sentiment: *' + str(res['user_sentiment']['label']) +
#                        '* with a score of ' + str(round(res['user_sentiment']['score'], 2)))
#
#    st.markdown('Topics: ' + ', '.join(res['user_topics']))
#
#    """
#    ---Our recommendation for you:
#    """
#    for song in res["songs"]:
#       if res["songs"]["cluster"] == 0:
#           song["cluster_label"] = "positive"
#       elif res["songs"]["cluster"] == 1:
#           song["cluster_label"] = "negative"
#       elif res["songs"]["cluster"] == 2:
#           song["cluster_label"] == "neutral"

#    for song in res["songs"]:
#
#        if res['user_sentiment']['label'] == song['sentiment_label'] == song["cluster_label"]:
#
#            url = f"https://open.spotify.com/embed/track/{song['id']}?utm_source=generator"
#
#            components.iframe(url, height=80)
#
#            st.markdown('Song cluster: '   + str(song['cluster']))
#            st.markdown('Song valence: '   + str(round(song['valence'], 2)))
#            st.markdown('Song sentiment: ' + str(song['sentiment_label']))
#            st.markdown('Song sentiment score: ' + str(round(song['sentiment_score'], 2)))
