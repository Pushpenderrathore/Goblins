#!/usr/bin/env bash
set -e

echo "🦞 Goblins AI Agent Installer"
echo "----------------------------------"

# 1️⃣ Check OS
if [[ "$OSTYPE" != "linux-gnu"* ]]; then
  echo "❌ This installer only supports Linux"
  exit 1
fi

# 2️⃣ Check systemd
if ! command -v systemctl &> /dev/null; then
  echo "❌ systemd not found"
  exit 1
fi

# 3️⃣ Check python
if ! command -v python3 &> /dev/null; then
  echo "❌ python3 not found. Install it first."
  exit 1
fi

# 4️⃣ Ask for API key (hidden input)
read -s -p "🔑 Enter your Moltbook API key: " MOLTBOOK_API_KEY
echo
if [[ ! "$MOLTBOOK_API_KEY" == moltbook_* ]]; then
  echo "❌ Invalid Moltbook API key format"
  exit 1
fi

# 5️⃣ Project path
PROJECT_DIR="$(pwd)"
PYTHON_BIN="$(which python3)"

echo "📁 Project directory: $PROJECT_DIR"

# 6️⃣ Create virtual environment
if [[ ! -d "venv" ]]; then
  echo "🐍 Creating virtual environment..."
  python3 -m venv venv
fi

source venv/bin/activate

# 7️⃣ Install dependencies
echo "📦 Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

deactivate

# 8️⃣ Create systemd service
SERVICE_FILE="/etc/systemd/system/goblins.service"

echo "🛠 Creating systemd service..."

sudo tee "$SERVICE_FILE" > /dev/null <<EOF
[Unit]
Description=Goblins AI Cyber Agent
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
User=$USER
WorkingDirectory=$PROJECT_DIR
Environment="MOLTBOOK_API_KEY=$MOLTBOOK_API_KEY"
ExecStart=$PROJECT_DIR/venv/bin/python main.py
Restart=always
RestartSec=60
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
EOF

# 9️⃣ Enable & start service
echo "🚀 Enabling and starting Goblins service..."
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl enable goblins.service
sudo systemctl restart goblins.service

echo
echo "✅ Installation complete!"
echo
echo "📌 Useful commands:"
echo "  systemctl status goblins.service"
echo "  journalctl -u goblins.service -f"
