FROM python:3.8.5-alpine3.12

ENV FLASK_ENV development
ENV PYTHONPATH /service/reflask

RUN apk add build-base openssl-dev libffi-dev postgresql-dev postgresql-client python3-dev yarn curl

RUN mkdir -p /service/reflask

COPY ./requirements/app.in /service/reflask/app.ini

RUN pip install -r /service/reflask/app.ini

COPY ./containers/flask/entrypoint.sh /entrypoint.sh

ENTRYPOINT /entrypoint.sh
