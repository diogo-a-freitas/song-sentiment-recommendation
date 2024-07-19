from transformers import pipeline

pipe = pipeline(model= "cardiffnlp/twitter-roberta-base-sentiment-latest")

def get_user_sentiment(text: str):

    return pipe(text)[0]
