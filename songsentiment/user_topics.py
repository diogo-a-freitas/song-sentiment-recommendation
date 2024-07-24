#import pickle
import pickle
from songsentiment.cleaning_user_input import  preprocessing
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import numpy as np
import random

#load lda model from picklefile // model was already trained on all twitter data and data is static
with open('model_small/lda_model_22_07_11_30.pkl', 'rb') as pickle_file:
    lda_model_22_07_11_30 = pickle.load(pickle_file)

#load vectorizer from picklefile // model was already fitted on all twitter data
with open('model_small/vectorizer_22_07_11_30.pkl', 'rb') as pickle_file:
    vectorizer_22_07_11_30 = pickle.load(pickle_file)

def pre_process_user_input(sentence, reverse_order=True):


    if reverse_order == True:
        #most probable topics
        top_word_ind = -1
        second_word_ind = -2
    else:
        #least probable topics
        top_word_ind = 0
        second_word_ind = 1

    #list to store top words
    top_words_list = []

    #clean user input with preprocessing steps
    processed_sentence = preprocessing(sentence)

    # Vectorize the user input

    #OUTPUT : (0, 2318)	0.2888112425753094, e.g
    #LOGIC: word at index 2318 in the vocabulary has a weight of 0.2888 in the vectorized sentence.
    vectorized_input = vectorizer_22_07_11_30.transform([processed_sentence])

    #OUTPUT: [0.00685844 0.00685844 0.00685844 0.00685844 0.00685844 0.00685844], etc -
    #LOGIC: a total of 40 numbers due to 40 components - maps input to each topic, it all adds up to 1.
    topic_distribution = lda_model_22_07_11_30.transform(vectorized_input)

    #OUTPUT: 20
    #LOGIC: outputs an integer which relates to most probable topic (0 indexed)
    #top_two_topics_indices = topic_distribution[0].argsort()[-2:][::-1]

    #most probable topic
    top_topics_indice = topic_distribution[0].argsort()[top_word_ind] #[-1]

    #second most probable topic
    top_two_topics_indice = topic_distribution[0].argsort()[second_word_ind] #[-2]

    # Get the top words for the most probable topic

    #OUTPUT: [2318  838 1323 1411  314]
    #LOGIC: Indices for the top words for the most probable topic - however, they refer to the indice in the vocabulary - unique words


    #GET WORDS FOR TOPICS
    #top words for most probable topic
    top_words_indices = lda_model_22_07_11_30.components_[top_topics_indice].argsort()[:-30 - 1:-1]

    #top words for second most probable
    second_top_words_indices = lda_model_22_07_11_30.components_[top_two_topics_indice].argsort()[:-30 - 1:-1]

    #GET WORDS

    words_with_weights = []

    #TOP TOPICS WORDS
    top_topic_words = [vectorizer_22_07_11_30.get_feature_names_out()[i] for i in top_words_indices]
    second_top_topic_words = [vectorizer_22_07_11_30.get_feature_names_out()[i] for i in second_top_words_indices]

    #GET WEIGHTS

    #top topic weights
    top_topic_weights = [lda_model_22_07_11_30.components_[top_topics_indice][i] for i in top_words_indices]
    #second topic weights
    second_top_topic_weights = [lda_model_22_07_11_30.components_[top_two_topics_indice][i] for i in second_top_words_indices]

    #TOPICS WITH WEIGHTS

    #first topic words and weights
    top_topic_words_with_weights = list(zip(top_topic_words, top_topic_weights))
    #first topic words and weights
    second_top_topic_words_with_weights = list(zip(second_top_topic_words, second_top_topic_weights))


    #Concatenate both lists

    topics_words_weights = top_topic_words_with_weights + second_top_topic_words_with_weights

    #get random 10

    random_10_words_weights = set(random.choices(topics_words_weights, k=10))
    sorted_random_10_words_weights = sorted(random_10_words_weights, key=lambda x: x[1], reverse=reverse_order)

    #get 5 from 10

    output_topics = sorted_random_10_words_weights[:5]

    #print out five words

    top_words = [x[0] for x in output_topics]

    #output_5_last = ', '.join(output_5)

    return top_words

print(pre_process_user_input("I am feeling happy"))
