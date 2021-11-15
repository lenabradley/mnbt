# https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04
# https://stackoverflow.com/questions/17413526/nginx-missing-sites-available-directory
# https://stackoverflow.com/questions/21740518/linux-ami-nginx-sites-enabled-missing
# so put in: /etc/nginx/conf.d/
sudo systemctl start myproject
sudo systemctl enable myproject

