# File Sharing Bot Telegram

Bot untuk menyimpan file ke database channel dan membuat link otomatis.

---

## 📦 Fitur
- Simpan file (dokumen, foto, video, audio) ke database channel
- Membuat link file otomatis
- Inline button admin panel:
  - ⚙️ Pengaturan → Admin Panel
  - 👤 Owner → langsung ke akun owner
  - 🛡 Force Sub, 📝 Start Text, 🔒 Protect Content, 📢 Broadcast, 👥 Users, 👤 Admins
- Broadcast ke semua user (hanya owner/admin)
- Protect konten untuk mencegah forward/download
- Daftar user & admin di MongoDB
- Support deploy Docker & manual GitHub
- Support `.env` untuk konfigurasi mudah

---

## 🚀 Deploy Docker
1. Update & install docker
```bash
apt -y update; apt -y install docker.io
docker login -u username -p token
docker run -d --name filesharingbot \
--env-file .env \
username/tag
docker logs -f filesharingbot
🖥 Deploy Manual GitHub
screen -S filesharingbot
git clone https://github.com/iandinoo/F5UB.git
cd F5UB
cp .env.example .env
nano .env
pip install -r requirements.txt
python3 start.py
