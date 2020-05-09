#!/bin/bash
sudo yum install git
sudo yum install python3
curl -O https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py --user

sudo yum install gcc -y
sudo yum install mysql-devel -y
sudo yum install python3-devel -y

pip install mysqlclient
pip install requests
pip install sqlalchemy


sudo yum install -y yum-utils
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
udo yum install docker-ce docker-ce-cli containerd.io -y
sudo systemctl start docker
sudo systemctl enable docker
sudo gpasswd -a $USER docker
newgrp docker

curl -L "https://github.com/docker/compose/releases/download/1.25.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose

mkdir -p mysql/data

