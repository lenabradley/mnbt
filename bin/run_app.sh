# https://medium.com/techfront/step-by-step-visual-guide-on-deploying-a-flask-application-on-aws-ec2-8e3e8b82c4f7
sudo ./venv/bin/gunicorn --bind 0.0.0.0:80 app:app