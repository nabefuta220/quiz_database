# quiz_database
5I情報工学実験　Webアプリ開発演習(1巡目)

## 開発環境

- python 3.10.4
- Django 2.2.7

## サーバーへの入り方

(準備)

1. モジュールをインストールする


```bash
python -m pip install -r requirements.txt
```

2. データを移行する

```bash
python manage.py migrate
```
3. 管理者ユーザーを作成する

```bash
python manage.py createsuperuser
(このあとはコマンドラインの指示にしたがって、ユーザー名、メールアドレス、パスワードを入力してください。)
```
4. ローカル上でサーバーを起動する

```bash
python manage.py runserver
(このあと、<http://127.0.0.1:8000/>にアクセスすることでサーバーが開けます。)
```