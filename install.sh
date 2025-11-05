#!/usr/bin/env bash
set -e

echo "🔧 Menginstal dependensi..."
if ! command -v python3 &> /dev/null; then
  echo "❌ Python3 belum terpasang. Silakan install dulu."
  exit 1
fi

python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install telethon
echo "✅ Instalasi selesai!"
echo "Jalankan dengan: ./run.sh"
