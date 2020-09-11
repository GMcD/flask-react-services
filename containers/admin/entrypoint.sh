#!/bin/sh

FLASK_APP=web.admin flask run --no-debugger --host 0.0.0.0 --port 7077 &

tail -f /dev/null
