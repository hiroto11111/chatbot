FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# 👇 spaCyの英語モデルを追加でインストール
RUN python -m spacy download en_core_web_sm

COPY . .

CMD ["python", "app.py"]
