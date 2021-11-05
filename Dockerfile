FROM tiangolo/uwsgi-nginx-flask

WORKDIR /app

ENV CONTAINERIZE_APP_1=main.py

ENV FLASK_RUN_HOST=0.0.0.0

COPY ./app/requirements.txt /app/

RUN pip3 install -r /app/requirements.txt

COPY ./app /app
