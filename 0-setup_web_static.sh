#!/usr/bin/env bash
# sets up web servers for deployment of web_static
sudo apt-get install nginx
if [ ! -d /data/web_static/releases/test/ ]; then
    sudo mkdir -p /data/web_static/releases/test/;
fi
simple_html="<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"
echo "$simple_html" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
SERVING="location /hbnb_static/ {\n\talias /data/web_static/current/;\n}"
sudo sed -i "39i $SERVING" /etc/nginx/sites-enabled/default
sudo service nginx restart
