from rclone_python import rclone
import os, time
from Json import load_json

def main():
  
  if rclone.is_installed():
    config = load_json('./config.json')
    while True:
      os.system('clear')
      rclone.sync(config['src_path'], config['dest_path'])
      time.sleep(config['time_sleep'])

if __name__ == '__main__':
  main()