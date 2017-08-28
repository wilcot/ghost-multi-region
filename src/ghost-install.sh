#!/bin/bash
sudo apt-get update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
sudo ufw allow 'Nginx Full'
curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash
sudo apt-get install -y nodejs
sudo npm i -g ghost-cli
sudo mkdir -p /var/www/ghost
sudo chown ubuntu:ubuntu /var/www/ghost
cd /var/www/ghost
INSTANCE_PUBLIC_URL=$(curl http://169.254.169.254/latest/meta-data/public-hostname)
ghost install --no-prompt --url "http://$INSTANCE_PUBLIC_URL" --dbhost RDS-URL --dbuser ghostadmin --dbpass RDS-PASSWORD