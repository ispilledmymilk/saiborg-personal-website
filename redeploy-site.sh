#!/bin/bash
set -e

PROJECT_DIR="$HOME/saiborg-personal-website"
SESSION_NAME="flask"

# Kill all existing tmux sessions (stops any running Flask server)
tmux kill-server 2>/dev/null || true

cd "$PROJECT_DIR"

# Sync with latest changes from GitHub main branch
git fetch
git reset --hard origin/main

# Enter virtual environment and install dependencies
source python3-virtualenv/bin/activate
pip install -r requirements.txt

# Start Flask in a new detached tmux session
tmux new-session -d -s "$SESSION_NAME"
tmux send-keys -t "$SESSION_NAME" "cd $PROJECT_DIR" Enter
tmux send-keys -t "$SESSION_NAME" "source python3-virtualenv/bin/activate" Enter
tmux send-keys -t "$SESSION_NAME" "export FLASK_APP=app" Enter
tmux send-keys -t "$SESSION_NAME" "export FLASK_ENV=development" Enter
tmux send-keys -t "$SESSION_NAME" "flask run --host 0.0.0.0 --port 5000" Enter
