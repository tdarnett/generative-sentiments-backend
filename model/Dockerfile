FROM ubuntu:xenial

RUN apt update && \
apt-get install -y curl && \
echo "deb http://storage.googleapis.com/tensorflow-serving-apt stable tensorflow-model-server tensorflow-model-server-universal" | tee /etc/apt/sources.list.d/tensorflow-serving.list && \
curl https://storage.googleapis.com/tensorflow-serving-apt/tensorflow-serving.release.pub.gpg | apt-key add - && \
apt update && \
apt-get install tensorflow-model-server

COPY data/sentiment-model /models/model

CMD tensorflow_model_server --port=8500 --rest_api_port=${PORT} --model_base_path=/models/model --model_name=saved_model