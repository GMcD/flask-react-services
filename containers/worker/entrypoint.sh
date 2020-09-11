#!/bin/sh

watchmedo auto-restart --directory=/service/reflask --pattern=*.py --recursive \
    -- celery worker -A web.application.clryrun:celery --loglevel=debug  &

tail -f /dev/null
