# ＜指定したアドレスにgmailからメールを送ってみよう編＞完成

import os
import smtplib
import ssl
from email.mime.text import MIMEText

# Gmailの環境設定（情報入力）
gmail_address = os.environ['gmail_add']  # gmailアドレスをpycharmの環境変数に入れた。
mail_key = os.environ['mail_key']  # gmailのPWをpycharmの環境変数に入れた。
receive_add = os.environ['receive_add']  # 相手先のﾒｱﾄﾞをpycharmの環境変数に入れた。

# Gmailの設定を書き込む
gmail_account = gmail_address
gmail_password = mail_key

# メールの送信先
mail_to = receive_add


def main():
    # メールデータ(MIME)の作成
    subject = "メール送信テスト"  # 件名の入力部分
    body = "pycharmからメール送信テストです。<br>一斉送信できるようになりたい。" \
           "<br>まずは宛先１件バージョン"  # 本文の部分
    msg = MIMEText(body, "html")
    msg["Subject"] = subject
    msg["To"] = mail_to
    msg["From"] = gmail_account

    # Gmailに接続
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465,
                              context=ssl.create_default_context())
    server.login(gmail_account, gmail_password)
    server.send_message(msg)  # メールの送信
    print("ok.")


if __name__ == '__main__':
    main()
