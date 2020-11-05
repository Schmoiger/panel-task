# to be run at instantiation of EC2
# either in

#!/bin/bash
sudo yum -y update
source activate pytorch_p36
sudo yum -y install ruby
sudo yum -y install wget
cd /home/ec2-user
wget https://aws-codedeploy-ap-south-1.s3.ap-south-1.amazonaws.com/latest/install
sudo chmod +x ./install
sudo ./install auto
sudo yum install -y python-pip
sudo python3 pip install --upgrade pip
sudo pip install awscli
