import os
import pickle  # type: ignore

import numpy as np  # type: ignore
import requests
from decouple import config  # type: ignore
from flask import Flask, jsonify, request  # type: ignore
from flask_cors import CORS  # type: ignore
from sklearn.preprocessing import LabelEncoder  # type: ignore

app = Flask(__name__)
CORS(app)

MAX_LENGTH: int = 100


@app.route("/predict/", methods=["POST"])
def sentiment_classifier() -> dict:
    # pre-process input text
    input_sentence = np.array([request.json["sentence"]])

    tokenizer = load_tokenizer()

    tokenized_sentence = pad_and_tokenize(tokenizer, input_sentence)

    # pass tokenized sentence to trained model
    prediction = predict(tokenized_sentence)

    confidence = np.max(prediction)
    label_idx = np.array([np.argmax(prediction)])

    # load the saved encoder classes so we can decode the label properly
    encoder = LabelEncoder()
    encoder.classes_ = np.load("assets/classes.npy", allow_pickle=True)
    label = encoder.inverse_transform(label_idx)

    # Returning JSON response to the frontend
    return jsonify(label=label[0], confidence=confidence, input_sentence=input_sentence[0])


def pad_and_tokenize(tokenizer, text: str) -> list:
    """
    pre-process the input sentence so that it matches the expected format of the NLP model.
    """
    sequences = tokenizer.texts_to_sequences(text)

    padded_data = np.pad(sequences[0], (max(MAX_LENGTH - len(sequences[0]), 0), 0), "constant").tolist()

    return padded_data


def load_tokenizer():
    with open("assets/tokenizer.pickle", "rb") as handle:
        tokenizer = pickle.load(handle)
    return tokenizer


def predict(tokenized_sentence: list) -> list:
    instances = [tokenized_sentence]
    body = {instances: instances}
    url = os.environ["PREDICT_URL"]

    response = requests.post(url, json=body)
    prediction_array = response.json()["predictions"][0]

    return prediction_array


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=config("PORT", default=8080, cast=int))
