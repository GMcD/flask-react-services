Certificates and Development
============================

Security on the Internet is paramount, and the wide scale adoption of HTTPS has supported this.
In turn, this has presented a number of development challenges, with various services requiring
valid certificates to function at all.
    * OAuth2
    * Notification API
    * Secure Cookies
to name but a few.

Using self-signed certificates, ngrok proxies, testing in staging environments
and a number of other workarounds has been common practice, but is an anti-pattern.

Running an SSL proxy container, with Let's Encrypt certificates on `localhost`
(yes, it is possible, with some magic), allows for local development behind secure
and trusted certificates, across multiple development machines, without configuration
changes.

The wildcard certificate here is used for SSL termination at the proxy for services,
and at the container for OAuth2.
