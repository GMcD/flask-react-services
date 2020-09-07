FROM postgres:12.4-alpine

RUN mkdir -p /docker-entrypoint-initdb.d

COPY ./containers/postgres/reflask.sql /docker-entrypoint-initdb.d
