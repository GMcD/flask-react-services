FROM postgres:12.4-alpine

RUN mkdir -p /docker-entrypoint-initdb.d

COPY ./containers/postgres/reflask.dump /docker-entrypoint-initdb.d
