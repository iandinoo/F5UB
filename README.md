# File Sharing Bot Telegram

## Deploy Docker Step by Step

1. apt -y update; apt -y install docker.io
2. docker login -u username -p token
3. docker run -d --name filesharingbot --env OWNER_ID=... --env DATABASE_CHANNEL=... --env API_ID=... --env API_HASH=... --env BOT_TOKEN="..." --env MONGO_URI="..." yannneedbj/fsubnew
4. docker logs -f filesharingbot
5. 
