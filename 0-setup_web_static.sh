#!/usr/bin/env bash
# Bash script that sets up the web servers for the deployment of web_static

# Install nginx if not installed
if [ $(dpkg-query -W -f='${Status}' nginx 2>/dev/null | grep -c "ok installed") -eq 0 ];
then
  apt update
  apt install -y nginx;
fi

# making required directories
mkdir -p /data;
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

# Dummy HTML file to test server config
echo "<html>\
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

# Create the specified symbolic link 
ln -s /data/web_static/releases/test/ /data/web_static/current

# Giving ownership of the /data/ folder to the ubuntu user AND group
chown -r ubuntu:ubuntu /data/

# Update the Nginx configuration file to serve the specified content
printf %s "server {
  root /data/web_static/current/;
  index index.html
  
  location /hbnb_static {
    alias /data/web_static/current/;
  }
} > /etc/nginx/sites-available/default

# reload & restart nginx
service nginx reload
service nginx restart
