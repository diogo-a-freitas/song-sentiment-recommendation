#import pickle
import pickle
from songsentiment.cleaning_user_input import  preprocessing
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import numpy as np

#load lda model from picklefile // model was already trained on all twitter data and data is static
with open('model_small/lda_model_first.pkl', 'rb') as pickle_file:
    lda_model = pickle.load(pickle_file)

#load vectorizer from picklefile // model was already fitted on all twitter data
with open('model_small/vectorizer_first.pkl', 'rb') as pickle_file:
    vectorizer = pickle.load(pickle_file)

#process the user input //applying vectorizing, LDA and cleaning function

def pre_process_user_input(sentence='My day was stressfull however i am happy that the machine learning model is performing better than it was before!!!!'):

    #top_5_words_from_top_topics = top_words_list[0]
    top_words_list = []

    #clean
    processed_sentence = preprocessing(sentence)

    # Vectorize the user input
    vectorized_input = vectorizer.transform([processed_sentence])

    # Predict the topic distribution for the vectorized input
    topic_distribution = lda_model.transform(vectorized_input)

    # Find the index of the most probable topic
    most_likely_topic_index = np.argmax(topic_distribution)

    # Get the top words for the most probable topic
    top_words_indices = lda_model.components_[most_likely_topic_index].argsort()[:-5 - 1:-1]
    top_words = [vectorizer.get_feature_names_out()[i] for i in top_words_indices]
    top_words_list.append(top_words[0:])
    return top_words_list[0]

print(pre_process_user_input())
