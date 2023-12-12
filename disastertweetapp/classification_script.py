import tensorflow as tf
from tensorflow.keras.models import load_model
from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences
from tensorflow import keras

import streamlit as st

import pickle
import pandas as pd

@st.cache_resource
def load_tokenizer():

    with open("models/lstm_token.pkl", "rb") as f:
        lstm_tokenizer = pickle.load(f)    

    return lstm_tokenizer

@st.cache_resource
def load_classifier():

    loaded_model = load_model("models/trained_lstm_model.h5", compile=False)

    return loaded_model 

def classify_tweets(tweet_text):

    model = load_classifier()
    tokenizer = load_tokenizer()


    encoded = pad_sequences(tokenizer.texts_to_sequences([tweet_text]), maxlen=100)

    result = model.predict(encoded)

    if result[0][0] >= 0.95:
        return {"status": "On-topic", "conf": result[0][0]}
    else:
        return {"status": "Off-topic", "conf": result[0][0]}

if __name__ == "__main__":

    model = load_classifier()


    print(classify_tweets("❌BREAKING❌ Unbelievable footage emerges of a mini hurricane in Leitrim today 😳 Thankfully no reports of injuries, but plenty of damage 😯 Follow us for more videos and share 🔄 #tornado #hurricane #leitrim"))
    print(classify_tweets("Get ready to rock ‘n’ roll with the fierce energy of “Hurricane”! This song will blow you away like a storm, leaving you craving more. Listen now at: https://bluillusionmusic.com/hurricane/ #rocknrollhurricane #hurricane #partywithhurricane #goodtimesrock #rockallnight #bluillusionmusic"))
    print(classify_tweets("With such an active hurricane season this year, I thought it appropriate to review what can happen if you are cruising during hurricane season. #cruise #cruisetips #hurricane #Caribbean https://sunhatsandchardonnay.com/hurricane-season-cruising-things-to-know/"))