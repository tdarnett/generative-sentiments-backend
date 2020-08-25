# Generative Sentiments - API

This directory contains a simple containerized flask app that provides the prediction API that interfaces with the NLP model created in the model directory.

Our model is hosted in GCP's AI Platform and the flask app is deployed to the same region as the model using Cloud Run.
 
I originally wanted to deploy my TF model using TF Serving, though since this is an NLP task I must preprocess the input string using the tokenizer trained for the model. Because of this, I've decided to wrap my TF model into a flask app and load the model, classes and tokenizer created from training into the served web-app. Hopefully I'll learn the better way to do this soon!


## Pushing New Tag

```shell script
git tag [TAG NUMBER]

git push origin [TAG NUMBER]
```