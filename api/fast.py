# TODO: Import your package, replace this by explicit imports of what you need
# from packagename.main import predict

from transformers import pipeline

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from songsentiment.interface.song_prediction import predict_songs

app = FastAPI()

#app.state.user_sentiment = pipeline(model= "cardiffnlp/twitter-roberta-base-sentiment-latest")

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

    final_df, user_sent, top_words_list = predict_songs(text)

    return {
        'user_sentiment': user_sent,
        'user_topics':    top_words_list,
        'songs':          final_df.to_dict(orient='records')
    }
