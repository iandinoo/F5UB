# File Sharing Bot Telegram

Fitur lengkap: Force Sub unlimited, Protect Content, Broadcast, Admin Panel, Custom Start Text.

---

## Deploy Docker Step by Step

1. Install Docker
```bash
apt -y update; apt -y install docker.io
docker login -u username -p token
docker run -d --name filesharingbot \
--env OWNER_ID=123456789 \
--env DATABASE_CHANNEL=-1001234567890 \
--env API_ID=123456 \
--env API_HASH="your_api_hash" \
--env BOT_TOKEN="your_bot_token" \
--env MONGO_URI="mongodb+srv://user:pass@cluster.mongodb.net/" \
yannneedbj/filesharingbot
docker logs -f filesharingbot
