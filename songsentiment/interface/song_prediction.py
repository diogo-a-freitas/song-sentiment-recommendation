
from songsentiment.user_topics import pre_process_user_input

def predict_songs(text_user: str):

    top_words_list = pre_process_user_input(text_user)

    return top_words_list
