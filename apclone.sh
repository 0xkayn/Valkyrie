#!/bin/bash

TOP_DIR=$PWD
git clone --shallow-submodules https://github.com/ArduPilot/ardupilot temppilot
cd temppilot && cat > .gitmodules <<EOF
[submodule "modules/uavcan"]
	path = modules/uavcan
	url = git://github.com/ArduPilot/uavcan.git
[submodule "modules/waf"]
	path = modules/waf
	url = git://github.com/ArduPilot/waf.git
[submodule "modules/gbenchmark"]
	path = modules/gbenchmark
	url = git://github.com/google/benchmark.git
[submodule "modules/mavlink"]
	path = modules/mavlink
	url = https://github.com/0xkayn/mavlink
[submodule "gtest"]
	path = modules/gtest
	url = git://github.com/ArduPilot/googletest
[submodule "modules/ChibiOS"]
	path = modules/ChibiOS
	url = git://github.com/ArduPilot/ChibiOS.git
[submodule "modules/libcanard"]
	path = modules/libcanard
	url = git://github.com/ArduPilot/libcanard.git
EOF
git submodule init && git submodule update
cat > ./modules/mavlink/.gitmodules <<EOF
[submodule "pymavlink"]
	path = pymavlink
	url = https://github.com/0xkayn/pymavlink
EOF
cd $TOP_DIR/temppilot/modules/mavlink/ && git submodule init && git submodule update
cd $TOP_DIR/temppilot/modules/uavcan/ && git submodule init && git submodule update

if [ -d "$TOP_DIR/ardupilot" ]; then
    rm -rf $TOP_DIR/ardupilot
    mv $TOP_DIR/temppilot $TOP_DIR/ardupilot
fi

cd $TOP_DIR
