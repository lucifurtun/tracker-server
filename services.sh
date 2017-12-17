#!/usr/bin/env bash

source `which virtualenvwrapper.sh`
workon tracker-server

function start() {
    redis-server &
    mosquitto &
    python manage.py mqtt
}

function stop() {
     echo "To be implemented..."
}


case $1 in
   "start") start;;
   "stop") stop;;
   *) echo "Unknown option!";;
esac
