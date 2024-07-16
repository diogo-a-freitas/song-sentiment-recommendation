# TODO: Import your package, replace this by explicit imports of what you need
# from packagename.main import predict

from transformers import pipeline

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.state.user_sentiment = pipeline(model= "cardiffnlp/twitter-roberta-base-sentiment-latest")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def root():
    return {
        'message': "Hi, the API is running!"
    }

@app.get("/predict")
def get_predict(text: str):

    prediction = app.state.user_sentiment(text)[0]

    return {
        'sentiment': prediction['label'],
        'score': prediction['score']
    }
