# Deploy to DigitalOcean VPS

Your VPS uses `redeploy-site.sh`, which pulls `origin/main` and restarts Flask in a tmux session on port 5000.

## After local changes

### 1. Push to `main` (laptop)

```bash
cd saiborg-personal-website
git checkout main
git push origin main
```

### 2. Redeploy on the VPS

```bash
ssh root@YOUR_DROPLET_IP
cd ~/saiborg-personal-website
./redeploy-site.sh
```

### 3. Verify

- Home: `http://YOUR_DROPLET_IP:5000/`
- Timeline: `http://YOUR_DROPLET_IP:5000/timeline/`

## First-time MySQL setup (if not done yet)

On the VPS:

```bash
sudo mysql
```

```sql
CREATE USER 'myportfolio'@'localhost' IDENTIFIED BY 'mypassword';
GRANT ALL PRIVILEGES ON *.* TO 'myportfolio'@'localhost';
FLUSH PRIVILEGES;
CREATE DATABASE myportfoliodb;
exit
```

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

Then run `./redeploy-site.sh` again.

## Troubleshooting

| Problem | Fix |
|---|---|
| Connection refused | `tmux attach -t flask` to see Flask logs; open port 5000 in DO firewall / `ufw` |
| MySQL errors | Check `.env` and `sudo systemctl status mysql` |
| Old code | Confirm `git push origin main` succeeded, then redeploy |
