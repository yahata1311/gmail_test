# 複数の人のメールを送ってみよう
# ＜添付ファイルを送ってみよう納期あり編＞kino
import datetime  # 日付ﾓｼﾞｭｰﾙ
import os
import smtplib  # メール送信ﾓｼﾞｭｰﾙ
import ssl  # SSL
from email import encoders  # 添付ファイルをメールで送るで送る為に変換ﾓｼﾞｭｰﾙ
from email.mime.base import MIMEBase
from email.mime.text import MIMEText  # 日本語送信ﾓｼﾞｭｰﾙ

# sys.stdout = codecs.getwriter("utf-8")(sys.stdout)  # エンコード指定
#
# Gmailの環境設定（情報入力）
gmail_address = os.environ['gmail_add']  # gmailアドレスをpycharmの環境変数に入れた。
mail_key = os.environ['mail_key']  # gmailのPWをpycharmの環境変数に入れた。
# receive_add = os.environ['receive_add']  # 相手先のﾒｱﾄﾞをpycharmの環境変数に入れた。
#
# メールの送信先
gmail_account = gmail_address
gmail_password = mail_key
#mail_to = receive_add
name = "矢羽田"
#
# 納期を自動でメールに記載したい時
today_date = datetime.date.today()  # 日付
delivery_date = today_date + datetime.timedelta(days=7)  # 納期７日後
# print(today_date, delivery_date)
#


import pandas as pd

df = pd.read_excel('mailing_list.xlsx')
df
# print()

for send_name, mail_to, filename in zip(df['宛名'], df['メールアドレス'], df['添付ファイル']):
    print(send_name, mail_to, filename)


def gmail_send(send_name, mail_to, filename):
    subject = "資料を送付させて頂きます。".format(send_name, to_date)

    body = '''いつもお世話になっております。<br>
            表題の資料をお送りします。,<br>
            ご確認お願い致します。<br><br>

            株式会社○○'''.format(delivery_date)

    msg = MIMEMulipart()

    msg['Subject'] = subject
    msg['TO'] = mail_to
    msg['From'] = gmail_account
    msg_body = MIMEText(body, "html")
    msg.attach(msg_body)

    # 添付ファイルを追加する（PDF）
    filename = "order_a.pdf"
    file = open(filename, "rb")

    # 添付ファイルの指定
    attachment_file = MIMEBase('application', 'pdf')
    attachment_file.set_payload((file).read())
    file.close()

    # 添付ファイルを添付させる
    encoders.encode_base64(attachment_file)
    attachment_file.add_header('Content - Disposition', "attachment", filename=filename)
    msg.attach(attachment_file)

    # SMTPサーバー
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context())
    server.login(gmail_account, gmail_password)
    server.send_message(msg)
    sarver.close()
    print(send_name, '様:送信完了')


if __name__ == '__gmail_send__':
    main()
