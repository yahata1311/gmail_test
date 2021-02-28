import os
import smtplib
import ssl
from email.mime.text import MIMEText


def main():
    gmail_address = os.environ['gmail_add']  # gmailアドレスをpycharmの環境変数に入れた。
    mail_key = os.environ['mail_key']  # gmailのPWをpycharmの環境変数に入れた。
    receive_add = os.environ['receive_add']  # 相手先のﾒｱﾄﾞをpycharmの環境変数に入れた。

    # 以下にGmailの設定を書き込む★ --- (*1)
    gmail_account = gmail_address
    gmail_password = mail_key

    # メールの送信先★ --- (*2)
    mail_to = receive_add

    # メールデータ(MIME)の作成 --- (*3)
    subject = "メール送信テスト"
    body = "pycharmからメール送信テストです。<br>一斉送信できるようになりたい。" \
           "<br>まずは宛先１件バージョン"
    msg = MIMEText(body, "html")
    msg["Subject"] = subject
    msg["To"] = mail_to
    msg["From"] = gmail_account

    # Gmailに接続 --- (*4)
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465,
                              context=ssl.create_default_context())
    server.login(gmail_account, gmail_password)
    server.send_message(msg)  # メールの送信
    print("ok.")


if __name__ == '__main__':
    main()
