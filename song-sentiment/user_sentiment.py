from transformers import pipeline

def get_user_sentiment(text: str):

    pipe = pipeline(model= "cardiffnlp/twitter-roberta-base-sentiment-latest")

    return pipe(text)[0]
