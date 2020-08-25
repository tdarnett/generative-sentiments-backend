FROM python:3.7-slim-buster

WORKDIR /usr/src/app

COPY src/ .

ENV GOOGLE_APPLICATION_CREDENTIALS=/usr/src/app/generative-sentiments-creds.json

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


CMD [ "python", "app.py" ]



