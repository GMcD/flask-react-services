#!/bin/sh

celery worker -A web.application.clryrun:celery --loglevel=debug  &

tail -f /dev/null
