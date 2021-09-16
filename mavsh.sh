#!/bin/bash


if [ $# -eq 0 ]; then
    echo "required parameters: 
    mode: gcs | rpi"
    exit 1
fi

mode=$1
if [ $mode == "gcs" ]; then
    echo "mavproxy.py --master= --source-system= --source-component= --quadcopter --load-module=mavsh --state-basedir='/mnt/hdd/projects/quads/mavlink/Valkyrie/logs' --aircraft=Valkyrie"

elif [ $mode == "rpi" ]; then
    echo "mavproxy.py --master= --quadcopter --load-module=mavsh --aircraft=Valkyrie"
fi

