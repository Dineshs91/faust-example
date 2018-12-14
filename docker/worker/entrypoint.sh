#! /bin/bash

sleep 20
faust -L eventlet -A faustapp worker -l info --without-web