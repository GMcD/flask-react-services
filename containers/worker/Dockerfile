ARG REGISTRY
ARG TAG_NO
FROM $REGISTRY/reflask/flask:$TAG_NO

COPY ./app/ /service/reflask

COPY ./containers/worker/entrypoint.sh /entrypoint.sh

WORKDIR /service/reflask

ENTRYPOINT /entrypoint.sh
