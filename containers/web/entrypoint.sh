#!/bin/sh

FLASK_APP=web.application flask run --no-debugger --host 0.0.0.0 --port 7079 \
    --cert /certs/local.projectscapa.com.crt --key /certs/local.projectscapa.com.key &

tail -f /dev/null
