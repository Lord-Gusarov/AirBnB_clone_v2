#!/usr/bin/env bash
# Sets up your web servers for the deployment of web_static
# --To be executed/ran with 'sudo'
apt-get update
apt-get -y install nginx
mkdir -p /data/web_static/releases/test/ /data/web_static/shared/
echo "<html><h1>Fake file, Nginx is Working!</h1></html>" | tee /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/

FILE="/etc/nginx/sites-available/default"
toMatch=$(grep '^\s*server_name' $FILE)
toAdd="$toMatch\n\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}"
sed -i "s#^$toMatch#$toAdd#" $FILE
service nginx restart
