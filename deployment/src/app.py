import pickle
import numpy as np
from flask import Flask, request, jsonify
from keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
import tensorflow as tf

# from flask_cors import CORS

app = Flask(__name__)

MAX_LENGTH = 100


# Uncomment this line if you are making a Cross domain request
# CORS(app)

# Testing URL
@app.route('/hello/', methods=['GET', 'POST'])
def hello_world():
    return 'Hello, World!'


@app.route('/predict/', methods=['POST'])
def sentiment_classifier():
    # pre-process input text
    input_sentence = np.array([request.data])

    model, tokenizer = load_model_resources()

    tokenized_sentence = pad_and_tokenize(tokenizer, input_sentence)

    # pass tokenized sentence to trained model
    prediction = model.predict(tokenized_sentence)
    #     print(prediction)

    confidence = np.max(prediction)
    label_idx = np.argmax(prediction)
    print(label_idx)

    result = np.array([label_idx])

    # load the saved encoder classes so we can decode the label properly
    encoder = LabelEncoder()
    encoder.classes_ = np.load('classes.npy', allow_pickle=True)

    label = encoder.inverse_transform(result)

    # Returning JSON response to the frontend
    return jsonify(label=label[0],
                   confidence=confidence,
                   input_sentence=input_sentence)


def pad_and_tokenize(tokenizer, text):
    sequences = tokenizer.texts_to_sequences(text)

    data = pad_sequences(sequences, maxlen=MAX_LENGTH)

    return data


def load_model_resources():
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    model = tf.keras.models.load_model('sentiment-model/')

    return model, tokenizer
