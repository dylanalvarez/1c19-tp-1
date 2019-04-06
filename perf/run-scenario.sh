#!/bin/sh
# bash run-scenario.sh root node

npm run artillery -- run $1.yaml -e $2
