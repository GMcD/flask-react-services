#!/bin/sh

celery worker -A web.application.celery --loglevel=debug  &

tail -f /dev/null
