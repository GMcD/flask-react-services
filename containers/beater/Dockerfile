ARG REGISTRY
ARG TAG_NO
FROM $REGISTRY/reflask/flask:$TAG_NO

ENV FLASK_APP web.application

COPY ./app/ /service/reflask

COPY ./containers/beater/entrypoint.sh /entrypoint.sh

WORKDIR /service/reflask

ENTRYPOINT /entrypoint.sh
