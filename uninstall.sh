#!/usr/bin/env bash
set -e

SERVICE_NAME="goblins.service"
SERVICE_FILE="/etc/systemd/system/$SERVICE_NAME"
PROJECT_DIR="$(pwd)"

echo "🗑️ Goblins AI Agent Uninstaller"
echo "----------------------------------"

# 1️⃣ Check systemd
if ! command -v systemctl &> /dev/null; then
  echo "❌ systemd not found"
  exit 1
fi

# 2️⃣ Stop service if running
if systemctl is-active --quiet "$SERVICE_NAME"; then
  echo "⏹ Stopping service..."
  sudo systemctl stop "$SERVICE_NAME"
else
  echo "ℹ️ Service not running"
fi

# 3️⃣ Disable service
if systemctl is-enabled --quiet "$SERVICE_NAME"; then
  echo "🚫 Disabling service..."
  sudo systemctl disable "$SERVICE_NAME"
else
  echo "ℹ️ Service not enabled"
fi

# 4️⃣ Remove service file
if [[ -f "$SERVICE_FILE" ]]; then
  echo "🧹 Removing systemd service file..."
  sudo rm -f "$SERVICE_FILE"
else
  echo "ℹ️ Service file not found"
fi

# 5️⃣ Reload systemd
echo "🔄 Reloading systemd..."
sudo systemctl daemon-reexec
sudo systemctl daemon-reload

# 6️⃣ Optional cleanup
echo
read -p "❓ Do you want to remove the Python virtual environment (venv)? [y/N]: " REMOVE_VENV
if [[ "$REMOVE_VENV" =~ ^[Yy]$ ]]; then
  rm -rf "$PROJECT_DIR/venv"
  echo "🗑️ venv removed"
else
  echo "ℹ️ venv kept"
fi

echo
read -p "❓ Do you want to remove cached Python files (__pycache__)? [y/N]: " REMOVE_CACHE
if [[ "$REMOVE_CACHE" =~ ^[Yy]$ ]]; then
  find "$PROJECT_DIR" -type d -name "__pycache__" -exec rm -rf {} +
  echo "🧹 cache cleaned"
else
  echo "ℹ️ cache kept"
fi

echo
echo "✅ Goblins AI Agent uninstalled successfully!"
echo
echo "📌 Project files are still here:"
echo "  $PROJECT_DIR"
echo
echo "You can safely delete the directory if you want:"
echo "  rm -rf $PROJECT_DIR"
