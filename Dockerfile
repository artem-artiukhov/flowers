FROM python:3.6-alpine

WORKDIR /app

COPY . /app

CMD python app.py