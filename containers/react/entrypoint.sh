#!/bin/sh

yarn install

# Patch Bug in legacy component..
ln -sf /service/react/node_modules/react-cardstack/dist/CardStack.js /service/react/node_modules/react-cardstack/dist/Cardstack.js

yarn start &

tail -f /dev/null
