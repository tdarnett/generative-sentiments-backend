FROM python:3.7-slim-buster

WORKDIR /usr/src/app

COPY src/ .

#ENV GOOGLE_APPLICATION_CREDENTIALS=/usr/src/app/generative-sentiments-creds.json

# hadolint ignore=DL3013
RUN pip install --upgrade pip
# hadolint ignore=DL3013
RUN pip install --no-cache-dir -r requirements.txt

# hadolint ignore=DL3025
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app