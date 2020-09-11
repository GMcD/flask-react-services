#!/bin/sh

celery beat -A web.application.clryrun:celery --loglevel=info --pidfile=/tmp/celerybeat.pid  &

tail -f /dev/null
