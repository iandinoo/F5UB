# File Sharing Bot (FINAL)

## Fitur
- Upload file oleh Admin/Owner
- Auto simpan ke Database Channel
- Generate link download
- Force Subscribe unlimited
- Protect Content ON/OFF
- Inline Button
- Broadcast (/gcast)
- Docker & Manual Deploy

---

## Deploy Manual
```bash
apt update
apt install python3 python3-pip -y
git clone REPO
cd F5UB
pip install -r requirements.txt
nano .env
python3 start.py

## Deploy Docker
apt -y update; apt -y install docker.io
docker login -u USERNAME -p TOKEN

docker run -d \
--name filesharingbot \
--env API_ID= \
--env API_HASH= \
--env BOT_TOKEN= \
--env OWNER_ID= \
--env DATABASE_CHAT_ID= \
--env MONGODB_URL= \
username/repo:tag
