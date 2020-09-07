ARG REGISTRY
ARG TAG_NO
FROM $REGISTRY/reflask/flask:$TAG_NO

COPY ./app/ /service/reflask

WORKDIR /service/reflask

COPY ./containers/web/entrypoint.sh /entrypoint.sh

EXPOSE 7079

ENTRYPOINT /entrypoint.sh
