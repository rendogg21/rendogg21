
FROM tiangolo/uwsgi-nginx-flask

WORKDIR /my_projectadhoc

ENV CONTAINERIZE_APP_1=server.py

ENV FLASK_RUN_HOST=0.0.0.0

COPY requirements.txt requirements.txt

COPY requirements.txt ./

RUN pip3 install -r requirements.txt

EXPOSE 8000

COPY . .

CMD [ "python3", "./server.py"]
