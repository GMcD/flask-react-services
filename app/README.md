Application Code
================

The code base for the Flask application is under `web`, and for the `react` interface, under `src`.

> TODO: Implement tests

Web
---

The code in `web` provides
    * `web.application` - Flask Blog App
    * `web.service` - Flask Post API
    * `blueprints.api` - Implementation of Post API for `web.service`
    * `blueprints.auth` - Implementation of OAuth2 and Users for `web.application`

The first two map to their respective containers. Each imports one of the blueprints.

> * The `blueprints.auth` blueprint needs SSL termination at the container, and should not need the database
> * The `web.application` does not need SSL at the container, and does need the database

> TODO: re-factor to Post users via API to Application.

Src
---

The code in `src` contains a very simple React app, with a CardStack component, to consume the Post API.
