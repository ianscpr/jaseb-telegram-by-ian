# ===============================================
# JASEB TELEGRAM BY IYAN (v2.0) - Aman & Simpel
# ===============================================

from telethon import TelegramClient
import asyncio
import time
import datetime
import os
import json

# ===============================================
# CONFIG LOAD (DARI config.json)
# ===============================================

CONFIG_FILE = 'config.json'

if not os.path.exists(CONFIG_FILE):
    print("❌ File 'config.json' tidak ditemukan.")
    print("Buat file 'config.json' seperti contoh di bawah ini:")
    print("""
{
  "API_ID": 123456,
  "API_HASH": "xxxxxxxxxxxxxxxx",
  "NOMOR_TELEPON": "+62xxxxxxxxxx",
  "NAMA_SESI": "session_anda",
  "TARGET": ["@nama_grup1", "@nama_grup2"],
  "PESAN_IKLAN": "Halo, ini pesan otomatis dari JASEB!",
  "DURASI_HARI": 10,
  "JEDA_ULANG": 0,
  "JEDA_PER_PESAN": 12
}
""")
    exit()

with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
    cfg = json.load(f)

API_ID = cfg.get("API_ID", 0)
API_HASH = cfg.get("API_HASH", "")
NOMOR_TELEPON = cfg.get("NOMOR_TELEPON", "")
NAMA_SESI = cfg.get("NAMA_SESI", "session_anda")
target_chats = cfg.get("TARGET", [])
PESAN_IKLAN = cfg.get("PESAN_IKLAN", "Tulis pesan iklan kamu di sini.")
RUN_DURATION = datetime.timedelta(days=cfg.get("DURASI_HARI", 10))
JEDA_ULANG = cfg.get("JEDA_ULANG", 0)
JEDA_PER_PESAN = cfg.get("JEDA_PER_PESAN", 12)

# ===============================================
# SISTEM BATAS WAKTU (10 HARI DEFAULT)
# ===============================================

STOP_DATE_FILE = 'bot_stop_target.txt'
current_time = datetime.datetime.now()

if not os.path.exists(STOP_DATE_FILE):
    stop_date = current_time + RUN_DURATION
    with open(STOP_DATE_FILE, 'w') as f:
        f.write(stop_date.isoformat())
    print(f"\n✅ TIMER BARU DITETAPKAN ({RUN_DURATION.days} hari).")
    print(f"   Bot berhenti otomatis pada: {stop_date.strftime('%Y-%m-%d %H:%M:%S')}\n")
else:
    with open(STOP_DATE_FILE, 'r') as f:
        stop_date = datetime.datetime.fromisoformat(f.read().strip())
    if current_time >= stop_date:
        print("\n🚨 BOT BERHENTI TOTAL! Hapus file 'bot_stop_target.txt' untuk restart.\n")
        exit()
    else:
        sisa = stop_date - current_time
        print(f"✅ Bot aktif. Sisa waktu: {sisa.days} hari, {(sisa.seconds // 3600)} jam.\n")

# ===============================================
# FUNGSI KIRIM PESAN
# ===============================================

async def kirim_iklan_user(client):
    if not target_chats:
        print("⚠️ ERROR: Daftar target kosong.")
        return

    print(f"📢 Mulai kirim ke {len(target_chats)} grup...")
    for chat_id in target_chats:
        try:
            await client.send_message(chat_id, PESAN_IKLAN, parse_mode='html')
            print(f"[✅ BERHASIL] {chat_id}")
            await asyncio.sleep(JEDA_PER_PESAN)
        except Exception as e:
            print(f"[❌ GAGAL] {chat_id}: {e}")
            await asyncio.sleep(30)

# ===============================================
# PROGRAM UTAMA
# ===============================================

async def main():
    client = TelegramClient(NAMA_SESI, API_ID, API_HASH)
    await client.start()

    if not await client.is_user_authorized():
        print("📱 Login pertama kali diperlukan.")
        await client.send_code_request(NOMOR_TELEPON)
        await client.sign_in(NOMOR_TELEPON, input("Masukkan kode verifikasi: "))

    print("✅ Terhubung ke akun Telegram.\n")

    while True:
        if datetime.datetime.now() >= stop_date:
            print("\n🚨 Batas waktu habis. Bot berhenti.")
            break

        await kirim_iklan_user(client)
        print("\n🔁 Siklus selesai. Mengulang lagi...\n")
        await asyncio.sleep(JEDA_ULANG)

if __name__ == '__main__':
    asyncio.run(main())
