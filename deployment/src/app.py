import pickle
import numpy as np
from flask import Flask, request, jsonify
from sklearn.preprocessing import LabelEncoder
from google.api_core.client_options import ClientOptions
from googleapiclient import discovery

# from flask_cors import CORS

app = Flask(__name__)

MAX_LENGTH = 100


# Uncomment this line if you are making a Cross domain request
# CORS(app)


@app.route('/predict/', methods=['POST'])
def sentiment_classifier():
    # pre-process input text
    input_sentence = np.array([request.json['sentence']])

    tokenizer = load_tokenizer()

    tokenized_sentence = pad_and_tokenize(tokenizer, input_sentence)

    # pass tokenized sentence to trained model
    prediction = predict(tokenized_sentence)

    confidence = np.max(prediction)
    label_idx = np.array([np.argmax(prediction)])

    # load the saved encoder classes so we can decode the label properly
    encoder = LabelEncoder()
    encoder.classes_ = np.load('assets/classes.npy', allow_pickle=True)
    label = encoder.inverse_transform(label_idx)

    # Returning JSON response to the frontend
    return jsonify(label=label[0],
                   confidence=confidence,
                   input_sentence=input_sentence[0])


def pad_and_tokenize(tokenizer, text):
    sequences = tokenizer.texts_to_sequences(text)

    padded_data = np.pad(sequences[0], (max(MAX_LENGTH - len(sequences[0]), 0), 0), 'constant').tolist()

    return padded_data


def load_tokenizer():
    with open('assets/tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
    return tokenizer


def predict(tokenized_sentence):
    model = 'generative_sentiments_model'
    project = 'generative-sentiments'
    instances = [tokenized_sentence]
    region = 'us-central1'
    version = 'v1'

    return predict_json(project, region, model, instances, version)


def predict_json(project, region, model, instances, version=None):

    prefix = "{}-ml".format(region) if region else "ml"
    api_endpoint = "https://{}.googleapis.com".format(prefix)

    client_options = ClientOptions(api_endpoint=api_endpoint)

    service = discovery.build('ml', 'v1', client_options=client_options)

    name = 'projects/{}/models/{}'.format(project, model)

    if version is not None:
        name += '/versions/{}'.format(version)

    response = service.projects().predict(
        name=name,
        body={'instances': instances}
    ).execute()

    if 'error' in response:
        raise RuntimeError(response['error'])

    return response['predictions']


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
