# First installation

1. Switch to root from sudoer account: `sudo -s`
1. Lock root account: `passwd -l root`
1. Edit SSH config: `nano /etc/ssh/sshd_config`
  a. Change SSH port and disable RootLogin.
  a. Setup an SSH key and disable PasswordAuthentication.
1. Install Nginx: `apt install -y nginx`
1. Configure firewall: `ufw allow [YOUR-SSH-PORT]; ufw allow 'Nginx Full'`
1. Start firewall: `ufw enable`
1. Make user account for the app: `adduser --system --home /srv/website website`
1. Clone repo from GitHub: `git clone https://github.com/tassaron/character-creator-htmx /srv/website`
1. Make Python virtual environment: `cd ~website; apt install -y python3-venv; python3 -m venv env`
1. Activate virtual environment: `source env/bin/activate`
1. Install using Pip: `pip install .`
1. Edit your domain name into this file: `nano setup/website.nginx`
  a. Standard practice is to name Nginx config files after the domain name, but it's not necessary
1. Place Nginx config: `cp setup/website.nginx /etc/nginx/sites-available/website.nginx`
1. Enable Nginx config: `ln -s /etc/nginx/sites-available/website.nginx /etc/nginx/sites-enabled/website.nginx`
1. Place Systemd unit: `cp setup/website.service /etc/systemd/system/website.service`
1. Set permissions: `chown -R website:www-data /srv/website; chmod -R 755 /srv/website`
1. Start uWSGI service: `systemctl start website.service`
1. Restart Nginx: `systemctl restart nginx`
1. Exit from root account: `exit`
1. At this point you can use [Certbot](https://certbot.eff.org/) to get an SSL cert that renews automatically, which also has a handy option to convert the Nginx config for you.
