# Generative Sentiments

![Project build](https://github.com/tdarnett/generative-sentiments-model/workflows/Project%20build/badge.svg)

The backend component of the [Generative Sentiments web app](https://github.com/tdarnett/generative-sentiments-web).

## Structure

This repo is comprised of two main directories:
1. [**Model**](/model/README.md) - mostly a jupyter notebook showing the development of the bidirectional LSTM NLP model used to predict emotions in a given sentence.
2. [**API**](/api/README.md) - a Flask app deployed on Google Cloud Run which exposes the prediction API consumed by the web app.

## Notes

This approach for both the ML model development and the deployment of the model we're taken largely as a learning exercise. I may change this over time, but purely for educational purposes. 
