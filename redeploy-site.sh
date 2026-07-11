#!/bin/bash
set -e

# 1. cd into project folder
cd "$HOME/saiborg-personal-website"

# 2. Sync VPS repo with latest main from GitHub
git fetch
git reset origin/main --hard

# 3. Enter virtual environment and install dependencies
source python3-virtualenv/bin/activate
pip install -r requirements.txt

# 4. Restart myportfolio systemd service
systemctl restart myportfolio
systemctl --no-pager --full status myportfolio | head -15

echo "==> Redeploy complete"
