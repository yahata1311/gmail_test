import codecs
import datetime  # 日付ﾓｼﾞｭｰﾙ
import smtplib  # メール送信ﾓｼﾞｭｰﾙ
import ssl
import sys
from email.mime.text import MIMEText  # 日本語送信ﾓｼﾞｭｰﾙ

sys.stdout = codecs.getwriter("utf-8")(sys.stdout)  # エンコード指定

gmail_account = "test@example.com"
gmail_password = パスワード
mail_to = "test@example.com"
name = "矢羽田"

# 納期を自動でメールに記載したい時
today_date = datetime.date.today()
delivery_date = today_date + datetime.timedelta(days=7)
print(today_date, delivery_date)

# 件名
subject = "{0}様、発注書の送付について".format(name)
body = "“{0}の発注書をお送りいたします。".format(date)

import pandas as pd

df = pd.read_excel('mailing_list.xlsx')
df

for send_name, mail_to, filename in zip(df['宛名'], df['メールアドレス'], df['添付ファイル']):
    print(send_name, mail_to, filename)


def gmail_send(send_name, mail_to, filename):
    subject = "{0}様、{1}の資料を送付させて頂きます。".format(send_name, to_date)

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

    filename = "order_a.pdf"
    file = open(filename, "rb")
    attachment_file = MIMEBase('application', 'pdf')
    attachment_file.set_payload((file).read())
    file.close()
    encoders.encode_base64(attachment_file)
    attachment_file.add_header('Content - Disposition', "attachment", filename=filename)
    msg.attach(attachment_file)

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context())
    server.login(gmail_account, gmail_password)
    server.send_message(msg)
