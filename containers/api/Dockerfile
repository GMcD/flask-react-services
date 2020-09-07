ARG REGISTRY
ARG TAG_NO
FROM $REGISTRY/reflask/flask:$TAG_NO

ENV FLASK_APP web.service

COPY ./app/ /service/reflask

WORKDIR /service/reflask

COPY ./containers/api/entrypoint.sh /entrypoint.sh

EXPOSE 7078

ENTRYPOINT /entrypoint.sh
