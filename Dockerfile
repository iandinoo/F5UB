FROM python:3.11-slim

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

ENV OWNER_ID=0
ENV DATABASE_CHANNEL=-1001234567890
ENV API_ID=0
ENV API_HASH=""
ENV BOT_TOKEN=""
ENV MONGO_URI=""

CMD ["python", "main.py"]
