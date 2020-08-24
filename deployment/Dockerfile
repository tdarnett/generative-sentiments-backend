FROM python:3.7-slim-buster

#RUN apt-get update && apt-get -y upgrade

WORKDIR /usr/src/app
#RUN ln -s /usr/include/locale.h /usr/include/xlocale.h

COPY src/ .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./app.py" ]



