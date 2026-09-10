#!/usr/bin/env bash
set -euo pipefail

echo "[Chrome install] Updating apt..."
sudo apt-get update -y

# Install prerequisites
echo "[Chrome install] Installing prerequisites..."
sudo apt-get install -y wget gnupg ca-certificates

# Add Google's signing key (idempotent)
KEYRING="/usr/share/keyrings/google-chrome.gpg"
if [ ! -f "$KEYRING" ]; then
  echo "[Chrome install] Adding Google signing key..."
  wget -q -O - https://dl.google.com/linux/linux_signing_key.pub \
    | sudo gpg --dearmor -o "$KEYRING"
else
  echo "[Chrome install] Google signing key already present."
fi

# Add Google Chrome repo (idempotent)
LIST_FILE="/etc/apt/sources.list.d/google-chrome.list"
if ! grep -q "dl.google.com/linux/chrome/deb" "$LIST_FILE" 2>/dev/null; then
  echo "[Chrome install] Adding Google Chrome apt repository..."
  echo "deb [arch=amd64 signed-by=$KEYRING] http://dl.google.com/linux/chrome/deb/ stable main" \
    | sudo tee "$LIST_FILE" > /dev/null
else
  echo "[Chrome install] Google Chrome apt repository already configured."
fi

echo "[Chrome install] Updating apt (with new repo)..."
sudo apt-get update -y

# Install Chrome
echo "[Chrome install] Installing google-chrome-stable..."
sudo apt-get install -y google-chrome-stable

echo "[Chrome install] Done. Version:"
google-chrome --version || echo "Chrome installed, but 'google-chrome' not on PATH?"