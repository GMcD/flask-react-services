FROM postgres:12.4-alpine

ARG POSTGRES_USER
ENV PGUSER $POSTGRES_USER

RUN mkdir -p /docker-entrypoint-initdb.d

COPY ./containers/postgres/reflask.sql /docker-entrypoint-initdb.d
