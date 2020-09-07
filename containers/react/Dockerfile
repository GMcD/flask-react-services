ARG REGISTRY
ARG TAG_NO
FROM $REGISTRY/reflask/flask:$TAG_NO

COPY ./app /service/react

WORKDIR /service/react

COPY ./containers/react/entrypoint.sh /entrypoint.sh

ENTRYPOINT /entrypoint.sh
