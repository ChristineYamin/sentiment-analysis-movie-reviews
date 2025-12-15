import streamlit as st
import joblib
import re
import string
from nltk.corpus import stopwords
import nltk
import os

nltk.download("stopwords")

# Load model & vectorizer
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, "sentiment_model.pkl")
vectorizer_path = os.path.join(BASE_DIR, "tfidf_vectorizer.pkl")

model = joblib.load(model_path)
tfidf = joblib.load(vectorizer_path)

stop_words = set(stopwords.words("english"))

def clean_text(text):
    text = re.sub(r"<.*?>", "", text)
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    words = [w for w in words if w not in stop_words]
    return " ".join(words)

st.title("Movie Review Sentiment Analysis")

user_input = st.text_area("Enter a movie review:")

if st.button("Predict Sentiment"):
    cleaned = clean_text(user_input)
    vectorized = tfidf.transform([cleaned])
    prediction = model.predict(vectorized)[0]

    if prediction == 1:
        st.success("Positive Review 😊")
    else:
        st.error("Negative Review 😞")
