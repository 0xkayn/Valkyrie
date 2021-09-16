#!/bin/bash

TOP_DIR=$PWD

if [ $# -eq 0 ]; then
    echo "argument required for update: pm | mp - Pymavlink | MAVProxy"
    exit 1
fi

if [[ $1 == "pm" && -d "$TOP_DIR/ardupilot/modules/mavlink/pymavlink" ]]; then
    cd $TOP_DIR/ardupilot/modules/mavlink/pymavlink && python3 setup.py install --user && cd $TOP_DIR
    
elif [[ $1 == "mp"  && -d "$TOP_DIR/MAVProxy" ]]; then
    cd $TOP_DIR/MAVProxy && python3 setup.py build install --user && cd $TOP_DIR
fi
    
