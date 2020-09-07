# Generative Sentiments - Model

This repository holds the jupyter notebook which implements a bidirectional LSTM model used to classify an emotional sentence into one of 6 emotions.

## Deployment Overview

This model is deployed using TFServing to a Cloud Run service.
TF Serving and Cloud Run don't play nicely together by default, so I had to customize the Dockerfile
 in order to support the proper port access.
  
Whenever a new tag is pushed to GitHub a Cloud Build is triggered which:
1. Builds the docker image specified in Dockerfile
2. Deploys the image to Cloud Run
3. Migrates all traffic to the new image once its stable

## Links

- Related projects:
  - [API backend for interfacing with this model](../api/README.md)
  - [Generative Sentiments Web App](https://github.com/tdarnett/generative-sentiments-web)

## Notes

The model is trained with data in the `/data/*.txt` files and saved to the sentiment-model directory.

My solution was heavily inspired by [this](https://www.kaggle.com/adithyansukumar/sentiment-analysis) bidirectional LSTM model created by kernel392aeb0326.
