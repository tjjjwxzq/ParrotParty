#!/bin/sh
while sleep 30; do phantomjs --ignore-ssl-errors=true --local-to-remote-url-access=true --web-security=false --ssl-protocol=any parrot-bot.js; done;
