from rclone_python import rclone
import os, time, datetime, asyncio
from Json import load_json
import smtplib
from email.mime.text import MIMEText

os.system('pyclean .')

def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")

def main():
  if rclone.is_installed():
    config = load_json('./config.json')
    subject = "DownloaderPi"
    
    while True:
      try:
        os.system('clear')
        rclone.sync(config['src_path'], config['dest_path'])
        text_send = f"DownloaderPi synchronization successful at {get_datetime()}"
        send_email(subject, text_send, config['sender'], config['recipients'], config['password'])
        time.sleep(config['time_sleep'])
      except KeyboardInterrupt:
        os.system('clear')
        break
      except:
        time.sleep(config['time_sleep'])


def get_datetime():
  current_datetime = datetime.datetime.now()
  formatted_datetime = current_datetime.strftime("%d-%m-%Y-%H-%M-%S")
  return formatted_datetime

  
if __name__ == '__main__':
  main()