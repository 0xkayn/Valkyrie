d sudo apt update && sudo apt -y upgrade
sudo apt remove -y python2 python3 

sudo apt-get install -y build-essential tk-dev libncurses5-dev \
libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev \
libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev

version=3.8.6

wget https://www.python.org/ftp/python/$version/Python-$version.tgz
tar zxf Python-$version.tgz
cd Python-$version
./configure --enable-optimizations
make -j4
sudo make altinstall
# holy fuck this takes so long to do on a pi0w...

sudo apt install -y python3-pip libxml2 libxml2-dev libxslt-dev
pip3 install dronekit pyserial



git clone https://github.com/Vuggo/Valkyrie
VPATH=$PWD/Valkyrie
cd Valkyrie/ardupilot/modules/mavlink/pymavlink
python3 setup.py install --user
cd $VPATH/MAVProxy
python3 setup.py build install --user

