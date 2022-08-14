from os import getenv
from dotenv import load_dotenv, dotenv_values
import smtplib
import email.message
@staticmethod
class Send_Email():

    def __init__(self):
        load_dotenv()
        self.connected = False


    def describe_send_email(self):
        print("Type: Mail Sender \n" \
               "Connection to server\n" \
               "Connected: {} \n".format(self.connected))

    def conect_server(self):
        try:
            connection = smtplib.SMTP(getenv("HOST"), getenv("PORT"))
            connection.starttls()
            connection.login(user=getenv("LOGIN"), password=getenv("PASSWORD"))
            self.connected = True
            return connection
        except smtplib.SMTPAuthenticationError as e:
            print(f"Code: {e.args[0]} - {e.args[1]}")
        except ConnectionRefusedError as e:
            print(f"Code: {e.args[0]} - {e.args[1]}")

    def send(self, connection):
        self.describe_send_email()
        try:
            msg = email.message.Message()
            msg['Subject'] = 'Enviando Email'
            msg['From'] = getenv('LOGIN')
            msg['To'] = 'leonardofgc@gmail.com'
            msg.add_header('Content-Type', 'text/html')
            connection.sendmail(from_addr=msg['From'], to_addrs=msg['To'], msg=msg.as_string().encode('utf-8'))
        except smtplib.SMTPRecipientsRefused as e:
            print(f"Code: {e.args[0]} - {e.args[1]}")
        except smtplib.SMTPRecipientsRefused as e:
            print(f"Code: {e.args[0]} - {e.args[1]}")

    def disconect_server(self, connection):
        connection.close()
        print("Connection closed")
