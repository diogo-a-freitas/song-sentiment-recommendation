# TODO: Import your package, replace this by explicit imports of what you need
# from packagename.main import predict

from transformers import pipeline

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.state.user_sentiment = pipeline(model= "cardiffnlp/twitter-roberta-base-sentiment-latest")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Endpoint for https://your-domain.com/
@app.get("/")
def root():
    return {
        'message': "Hi, the API is running!"
    }

# Endpoint for https://your-domain.com/predict?input_one=154&input_two=199
@app.get("/predict")
def get_predict(text: str):

    prediction = app.state.user_sentiment(text)[0]

    return {
        'sentiment': prediction['label'],
        'score': prediction['score']
    }
