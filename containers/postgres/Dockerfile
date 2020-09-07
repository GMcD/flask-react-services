FROM postgres:12.4-alpine

RUN mkdir -p /docker-entrypoint-initdb.d

COPY ./containers/postgres/reflask.v1.dump /docker-entrypoint-initdb.d
