🧠 JASEB TELEGRAM BY IAN

Otomatis kirim pesan / iklan ke banyak grup Telegram dengan mudah dan aman.

⚙️ FITUR UTAMA

✅ Kirim pesan otomatis ke banyak grup sekaligus
✅ Aman — ada batas waktu jalan (default 10 hari)
✅ Support akun pribadi (bukan bot token)
✅ Bisa jalan di Termux, Git Bash, atau PC/Laptop (Windows/Linux)
✅ Setting gampang lewat config.json
✅ Tidak perlu tulis ulang kode, cukup edit file konfigurasi

📁 STRUKTUR FILE
📦 jaseb-telegram-by-ian
 ┣ 📜 jaseb.py          → Script utama
 ┣ 📜 install.sh        → Script instalasi otomatis
 ┣ 📜 run.sh            → Jalankan bot dengan sekali klik
 ┣ 📜 config.json       → Data akun & pengaturan
 ┗ 📜 .gitignore        → Mengabaikan file sensitif

⚡ CARA PAKAI (UNTUK TERMUX / LINUX / GIT BASH)
1️⃣ Install bahan:
pkg update && pkg upgrade -y
pkg install python git -y
pip install telethon

2️⃣ Clone repository:
git clone https://github.com/Bangiyan978/jaseb-telegram-by-ian.git
cd jaseb-telegram-by-ian

3️⃣ Edit pengaturan:
nano config.json


Isi dengan data kamu:

{
  "API_ID": 123456,
  "API_HASH": "xxxxxxxxxxxxxxxx",
  "NOMOR_TELEPON": "+62xxxxxxxxxx",
  "NAMA_SESI": "session_anda",
  "TARGET": ["@namagrup1", "@namagrup2"],
  "PESAN_IKLAN": "Halo, ini pesan otomatis dari JASEB!",
  "DURASI_HARI": 10,
  "JEDA_ULANG": 0,
  "JEDA_PER_PESAN": 12
}


🔒 Catatan Penting:
Jangan upload config.json ke GitHub publik karena berisi data pribadi (API & nomor).

4️⃣ Jalankan bot:
python jaseb.py


💡 Kalau pertama kali login, kamu bakal diminta kode verifikasi dari Telegram.

🧩 OPSI INSTALASI OTOMATIS

Kalau kamu pengen lebih cepat:

bash install.sh
bash run.sh

⚠️ PERINGATAN

Gunakan script ini secara bijak dan tidak untuk spam berlebihan.

Telegram bisa membatasi akun jika mengirim pesan ke grup secara massal terlalu cepat.

Disarankan pakai jeda antar pesan (JEDA_PER_PESAN) minimal 10–15 detik.

Gunakan akun cadangan jika ingin eksperimen.

🧑‍💻 PEMBUAT

Script ini dibuat oleh Ian

🔗 GitHub: Bangiyan978
💬 KONTAK / SUPPORT

Kalau butuh bantuan, update, atau mau request fitur baru:
📩 Telegram: @Yanscpr
