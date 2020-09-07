ARG REGISTRY
ARG TAG_NO
FROM $REGISTRY/reflask/flask:$TAG_NO

COPY ./app/ /service/reflask

RUN mkdir -p /certs

COPY ./keys/local.projectscapa.com.crt ./keys/local.projectscapa.com.key /certs/

WORKDIR /service/reflask

COPY ./containers/web/entrypoint.sh /entrypoint.sh

EXPOSE 7079

ENTRYPOINT /entrypoint.sh
