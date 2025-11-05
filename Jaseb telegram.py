# jaseb.py
from telethon import TelegramClient
import asyncio
import time
import datetime
import os

# ===============================================
# --- PENGATURAN WAKTU UTAMA (BATAS MAKSIMAL) ---
# ===============================================

STOP_DATE_FILE = 'bot_stop_target.txt'
RUN_DURATION = datetime.timedelta(days=10)
JEDA_ULANG = 0

current_time = datetime.datetime.now()
stop_date = None

if not os.path.exists(STOP_DATE_FILE):
    stop_date = current_time + RUN_DURATION
    with open(STOP_DATE_FILE, 'w') as f:
        f.write(stop_date.isoformat())
    print(f"\n✅ TIMER BARU DITETAPKAN ({RUN_DURATION.days} hari).")
    print(f"   Bot berhenti otomatis pada: {stop_date.strftime('%Y-%m-%d %H:%M:%S')}\n")
else:
    with open(STOP_DATE_FILE, 'r') as f:
        stop_date_str = f.read().strip()
    stop_date = datetime.datetime.fromisoformat(stop_date_str)
    if current_time >= stop_date:
        print("\n🚨 BOT BERHENTI TOTAL! Hapus file 'bot_stop_target.txt' untuk restart.\n")
        exit()
    else:
        sisa = stop_date - current_time
        print(f"✅ Bot aktif. Sisa waktu: {sisa.days} hari, {(sisa.seconds//3600)} jam.\n")

# ===============================================
# DATA AKUN TELEGRAM ANDA
# ===============================================

API_ID = 0  # Ganti dengan API_ID Anda
API_HASH = ''  # Ganti dengan API_HASH Anda
NOMOR_TELEPON = ''  # Ganti dengan nomor telepon (+62...)
NAMA_SESI = 'session_anda'

# ===============================================
# TARGET GRUP
# ===============================================

target_chats = [
    # Contoh: '@nama_grup1', '@nama_grup2'
]

# ===============================================
# PESAN IKLAN
# ===============================================

PESAN_IKLAN = """Tulis pesan iklan kamu di sini."""

# ===============================================
# FUNGSI UTAMA
# ===============================================

async def kirim_iklan_user(client):
    JEDA_PER_PESAN = 12
    if not target_chats:
        print("⚠️ ERROR: Daftar target kosong.")
        return

    print(f"Mulai kirim ke {len(target_chats)} grup...")
    for chat_id in target_chats:
        try:
            await client.send_message(chat_id, PESAN_IKLAN, parse_mode='html')
            print(f"[OK] {chat_id}")
            await asyncio.sleep(JEDA_PER_PESAN)
        except Exception as e:
            print(f"[GAGAL] {chat_id}: {e}")
            await asyncio.sleep(30)

async def main():
    client = TelegramClient(NAMA_SESI, API_ID, API_HASH)
    await client.start()

    if not await client.is_user_authorized():
        print("Login pertama kali diperlukan.")
        await client.send_code_request(NOMOR_TELEPON)
        await client.sign_in(NOMOR_TELEPON, input("Masukkan kode verifikasi: "))

    print("✅ Terhubung ke akun Telegram.\n")

    while True:
        global stop_date
        if stop_date and datetime.datetime.now() >= stop_date:
            print("\n🚨 Batas waktu habis. Bot berhenti.")
            break

        await kirim_iklan_user(client)
        print("\n🔁 Ulangi siklus...")
        await asyncio.sleep(JEDA_ULANG)

if __name__ == '__main__':
    asyncio.run(main())
