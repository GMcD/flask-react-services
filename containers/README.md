Deployment of Containers
========================

Again, unconventionally, this component uses a Makefile to inject an environment into
the `docker-compose build` process. Thus each container set has a defined environment,
common across all development, testing or staging machines (if so required).

# Build

The `reflask-build.yml` docker compose file provides for building all the containers.

# Environment

The `reflask-env.txt` is injected by the `Makefile` into each `make build`, ensuring consistent
environment settings in the container set.

> Note, this file will have siblings, `reflask-env-dev.txt`, `reflask-env-integration.txt`, and
so forth, to build container sets with distinct environments.

# Run

The `reflask-run.yml` docker compose file provides for running all the containers, complete with
volumes, network and services,

# Containers

The individual containers are deployed with `make up` and `make down`.

## Flask

 The `flask` container is built off `python:3.8.5-alpine3.12` and installs `app.in` requirements.

  > This should be a multistage build, to reduce container size

## API

  The `api` container deploys the `web.service` flask micro service, which serves up `/v2/posts`

## Postgres

  The `postgres` container contains a backup of some initial data for testing, similar to how
  fixtures are typically used. The app will function perfectly, without this sample data, so
  it is only here for developer efficiency.

## Proxy SSL
  The `proxy-ssl` container provides for SSL termination as required.

## React
  The `react` container runs WDS to allow hot reload from the local filesystem.

## Web
  The `web` container deploys the `wee.application` flask app for authoring posts.
