#!/usr/bin/env bash
# Redeploy the portfolio site on the VPS.
# Run from the project root on the server: ./redeploy-site.sh
set -euo pipefail

APP_DIR="${APP_DIR:-$HOME/saiborg-personal-website}"
BRANCH="${BRANCH:-main}"
SERVICE_NAME="${SERVICE_NAME:-portfolio}"

cd "${APP_DIR}"

echo "==> Pulling latest code (${BRANCH})"
git fetch origin
git checkout "${BRANCH}"
git pull origin "${BRANCH}"

if [[ ! -f .env ]]; then
  echo "ERROR: .env is missing. Run: cp example.env .env  and fill in MySQL + URL values."
  exit 1
fi

echo "==> Setting up virtualenv + dependencies"
if [[ ! -d python3-virtualenv ]]; then
  python3 -m venv python3-virtualenv
fi
# shellcheck disable=SC1091
source python3-virtualenv/bin/activate
pip install -r requirements.txt

echo "==> Restarting ${SERVICE_NAME} service"
if systemctl list-unit-files | grep -q "^${SERVICE_NAME}.service"; then
  sudo systemctl restart "${SERVICE_NAME}"
  sudo systemctl status "${SERVICE_NAME}" --no-pager -l | head -20
else
  echo "WARNING: systemd unit ${SERVICE_NAME}.service not found."
  echo "Start manually with:"
  echo "  source python3-virtualenv/bin/activate"
  echo "  export FLASK_APP=app"
  echo "  gunicorn --bind 0.0.0.0:5000 app:app"
fi

echo "==> Redeploy complete"
