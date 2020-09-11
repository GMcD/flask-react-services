Requirements
============

Updating repository requirements is often seen as expensive and unnecessary. However, this leads
to a cycle of increasing technical debt, and is an anti-pattern.

Once a Container is built and tagged using a set of requirements, there is no reason to rebuild that
container again. The next iteration of the container should contain the stable release of the
top level requirements, and any upgrade issues should be dealt with at the same time as the fix.

> pyup-bot.io is an example of this philosophy

As such, the build process uses `app.in`, and will automatically generate `requirements.txt`.
