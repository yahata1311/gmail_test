# ＜gmailからファイルを添付して送ってみよう編＞ひとまず完成☆

# email送信モジュール
import os
import smtplib  # メール送信ﾓｼﾞｭｰﾙ
import ssl  # SSL
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText  # 日本語送信ﾓｼﾞｭｰﾙ
from os.path import basename  # ﾊﾟｽの中からファイル名を取得する。

# Gmailの環境設定（情報入力）
gmail_address = os.environ['gmail_add']  # gmailアドレスをpycharmの環境変数に入れた。
mail_key = os.environ['mail_key']  # gmailのPWをpycharmの環境変数に入れた。
receive_add = os.environ['receive_add']  # 相手先のﾒｱﾄﾞをpycharmの環境変数に入れた。

# Gmailの設定を書き込む
gmail_account = gmail_address
gmail_password = mail_key


# ここからメールの内容

def main():
    # メールの本文
    message = 'メールテスト添付バージョン'
    # メールの内容を作成
    msg = MIMEMultipart()
    # 件名
    msg['Subject'] = '件名内容'
    # メール送信元
    msg['From'] = gmail_account
    # メール送信先
    msg['To'] = receive_add

    # ファイルを添付
    msg.attach(MIMEText(message))
    # ファイルを添付
    path = "./test.txt"
    with open(path, "rb") as f:
        part = MIMEApplication(
            f.read(),
            Name=basename(path)
        )
    part['Content-Disposition'] = 'attachment; filename="%s"' % basename(path)
    msg.attach(part)

    # Gmailに接続
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465,
                              context=ssl.create_default_context())
    server.login(gmail_account, gmail_password)
    server.send_message(msg)  # メールの送信
    print("ok.")


if __name__ == '__main__':
    main()
