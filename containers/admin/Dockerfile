ARG REGISTRY
ARG TAG_NO
FROM $REGISTRY/reflask/flask:$TAG_NO

ENV FLASK_APP web.admin

COPY ./app/ /service/reflask

COPY ./containers/admin/entrypoint.sh /entrypoint.sh

WORKDIR /service/reflask

ENTRYPOINT /entrypoint.sh
