#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static
sudo apt-get -y update
sudo apt-get install -y nginx
if [ ! -d /data/web_static/releases/test/ ]; then
    sudo mkdir -p /data/web_static/releases/test/;
fi
if [ ! -d /data/web_static/releases/test/ ]; then
    sudo mkdir -p /data/web_static/shared/;
fi
boiler="<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"
echo "$boiler" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
serve="location /hbnb_static/ {\n\talias /data/web_static/current/;\n}"
sudo sed -i "39i $serve" /etc/nginx/sites-enabled/default
sudo service nginx restart