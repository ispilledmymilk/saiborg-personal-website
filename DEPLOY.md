# Deploy to DigitalOcean VPS

This guide gets the Flask + MySQL timeline site running on your droplet.

## 1. Merge to `main` (on your laptop)

```bash
cd saiborg-personal-website
git checkout main
git pull origin main
git merge feature/projects-page
git push origin main
```

Or merge the open PR on GitHub into `main`.

## 2. SSH into the droplet

```bash
ssh root@YOUR_DROPLET_IP
```

(Use your DigitalOcean IP from the droplet dashboard.)

## 3. Install system packages (one-time)

```bash
apt update
apt install -y git python3 python3-venv python3-pip mysql-server
```

## 4. Clone the repo (one-time)

```bash
cd ~
git clone https://github.com/ispilledmymilk/saiborg-personal-website.git
cd saiborg-personal-website
```

If the repo is private, use a [personal access token](https://github.com/settings/tokens) or SSH key.

## 5. Set up MySQL (one-time)

```bash
sudo mysql
```

Inside MySQL:

```sql
CREATE USER 'myportfolio'@'localhost' IDENTIFIED BY 'mypassword';
GRANT ALL PRIVILEGES ON *.* TO 'myportfolio'@'localhost';
FLUSH PRIVILEGES;
CREATE DATABASE myportfoliodb;
exit
```

## 6. Create `.env` on the VPS (one-time)

```bash
cd ~/saiborg-personal-website
cp example.env .env
nano .env
```

Set:

```
URL=YOUR_DROPLET_IP:5000
MYSQL_HOST=localhost
MYSQL_USER=myportfolio
MYSQL_PASSWORD=mypassword
MYSQL_DATABASE=myportfoliodb
```

If you have a domain (e.g. DuckDNS), use `your-domain:5000` instead of the IP.

## 7. Firewall — open port 5000 (one-time)

```bash
ufw allow OpenSSH
ufw allow 5000/tcp
ufw enable
ufw status
```

Also allow **TCP 5000** in the DigitalOcean firewall (Networking → Firewalls) if one is attached.

## 8. Install systemd service (one-time)

Edit paths in `portfolio.service` if your home directory is not `/root`:

```bash
sudo cp ~/saiborg-personal-website/portfolio.service /etc/systemd/system/portfolio.service
sudo systemctl daemon-reload
sudo systemctl enable portfolio
```

## 9. Redeploy (every update)

```bash
cd ~/saiborg-personal-website
chmod +x redeploy-site.sh
./redeploy-site.sh
```

## 10. Verify

- Home: `http://YOUR_DROPLET_IP:5000/`
- Timeline: `http://YOUR_DROPLET_IP:5000/timeline/`

## Troubleshooting

| Problem | Fix |
|---|---|
| Connection refused | Check `sudo systemctl status portfolio` and firewall |
| MySQL error on start | Confirm `.env` credentials; `sudo systemctl status mysql` |
| Old code showing | `git pull` on `main`, then `./redeploy-site.sh` |
| Port already in use | `sudo lsof -i :5000` then kill/restart the service |

## After every local change

```bash
# laptop
git push origin main

# VPS
ssh root@YOUR_DROPLET_IP
cd ~/saiborg-personal-website && ./redeploy-site.sh
```
