#!/usr/bin/env bash
# Bash script that sets up the web servers for the deployment of web_static

# Install nginx if not installed
if [ $(dpkg-query -W -f='${Status}' nginx 2>/dev/null | grep -c "ok installed") -eq 0 ];
then
  apt update
  apt install -y nginx
fi

# making required directories
mkdir -p /data;
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

# Dummy HTML file to test server config
printf %s "<!DOCTYPE html>
<html>
   <head>
   </head>
   <body>
     Holberton School
   </body>
 </html>" | tee /data/web_static/releases/test/index.html

# Create the specified symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Giving ownership of the /data/ folder to the ubuntu user AND group
chown -R ubuntu:ubuntu /data

# Update the Nginx configuration file to serve the specified content
sed -i '39 i\ \tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n' /etc/nginx/sites-enabled/default

sudo service nginx restart


