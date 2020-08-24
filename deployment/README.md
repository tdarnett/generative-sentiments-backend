# Generative Sentiments - Deployment

Simple lambda function triggered by POST API requests containing
 a english sentence and feeding the sentence into a trained NLP model.
 
# Usage

1. Install npm dependencies with `npm install`
2. API logic can be edited in `handler.py`
3. Run `serverless deploy`

I originally wanted to deploy my TF model using TF Serving, though since this is an NLP task I must preprocess the input string using the tokenizer trained for the model. Because of this, I've decided to wrap my TF model into a flask app and load the model, classes and tokenizer created from training into the served web-app. Hopefully I'll learn the better way to do this soon!
