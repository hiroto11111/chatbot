# 分散システム Chatbot アプリケーション

このリポジトリは、Flask と ChatterBot を用いたシンプルなチャットボット Web アプリケーションです。  
Docker を利用して環境構築・実行が可能です。

## 構成

- `app.py` : Flask アプリケーション本体
- `requirements.txt` : 必要な Python パッケージ一覧
- `Dockerfile` : Docker 用ビルドファイル
- `templates/index.html` : チャット画面の HTML テンプレート

## 構築手順

### 1. Docker のインストール
Docker がインストールされていない場合は、[公式サイト](https://www.docker.com/)からインストールしてください。

### 2. イメージのビルドとコンテナの起動
ターミナルでプロジェクトディレクトリに移動し、以下のコマンドを実行します。

- docker build -t chatbot .
- docker run -p 5000:5000 chatbot
　
### 3. ブラウザでアクセス

ブラウザで[URL](http://127.0.0.1:5000/)にアクセスするとチャットボット画面が表示されます。

## 注意点

- 初回起動時は ChatterBot のコーパス学習に時間がかかる場合があります。
- ChatterBot の英語コーパスのみを利用しています（日本語未対応）。
