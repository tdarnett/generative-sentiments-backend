# Generative Sentiments - API

This directory contains a simple containerized flask app that provides the prediction API that interfaces with the NLP model created in the model directory.

## Deployment Overview

This API is deployed to a cloud run service located in the same region as the model cloud run service.

Whenever a new tag is pushed to GitHub a Cloud Build is triggered which:
1. Builds the docker image specified in Dockerfile
2. Deploys the image to Cloud Run
3. Migrates all traffic to the new image once its stable

### Pushing Tags
```shell
$ git tag v[TAG NUMBER]
$ git push origin v[TAG NUMBER]
```

## Links

- Related projects:
  - [Bi-directional LSTM NLP Model](../model/README.md)
  - [Generative Sentiments Web App](https://github.com/tdarnett/generative-sentiments-web)

