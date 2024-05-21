from rclone_python import rclone
import os, time, telegram, datetime, asyncio
from Json import load_json
os.system('pyclean .')

def main():
  if rclone.is_installed():
    config = load_json('./config.json')
    bot = telegram.Bot(token=config['api_key'])
    
    while True:
      try:
        os.system('clear')
        rclone.sync(config['src_path'], config['dest_path'])
        text_send_telegram = f"DownloaderPi synchronization successful at {get_datetime()}"
        asyncio.run(send_mail(bot, config, text_send_telegram))
        time.sleep(config['time_sleep'])
      except KeyboardInterrupt:
        os.system('clear')
        break
      except:
        pass


def get_datetime():
  current_datetime = datetime.datetime.now()
  formatted_datetime = current_datetime.strftime("%d-%m-%Y-%H-%M-%S")
  return formatted_datetime

async def send_mail(bot, config, text_send_telegram):
  return await bot.send_message(chat_id=config['chat_id'], text=text_send_telegram)
  
if __name__ == '__main__':
  main()