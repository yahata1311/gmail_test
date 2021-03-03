# 複数の人のメールを送ってみよう

import smtplib
import ssl
from email.mime.text import MIMEText

import pandas as pd

df = pd.read_excel('mailing_list.xlsx')
df

# カラム取り出し
for send_name, mail_to, filename in zip(df['宛名'], df['メールアドレス'], df['添付ファイル']):
    print(send_name, mail_to, filename)


# 関数定義
def gmail_send(send_name, mail_to, filename):
    subject = "{0}様、{1}の資料を送付させて頂きます。".format(send_name, today_date)
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

    filename = filename  # ファイル名
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
    server.close()
    print(send_name, '様：送信完了')


for send_name, mail_to, filename in zip(df['宛名'], df['メールアドレス'], df['添付ファイル']):
    gmail_send(send_name, mail_to, filename)
