#!/usr/bin/env bash
# Bash script that sets up the web servers for the deployment of web_static

# Install nginx if not installed
apt update
apt install -y nginx;

# making required directories
sudo mkdir -p /data;
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# Dummy HTML file to test server config
printf %s "<html>
   <head>
   </head>
   <body>
     Holberton School
   </body>
 </html>" | sudo tee /data/web_static/releases/test/index.html

# Create the specified symbolic link
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# Giving ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration file to serve the specified content
sudo chmod 755 /etc/nginx/sites-available/default
printf %s "server {
  listen 80;
  listen [::]:80;

  server_name _;
  root /data/web_static/current;
  index index.html;

  location /hbnb_static {
    alias /data/web_static/current/;
  }
}" > /etc/nginx/sites-available/default

sudo service nginx reload
sudo service nginx restart
