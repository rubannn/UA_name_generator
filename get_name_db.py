# https://generatefakename.com/ru/name/random/uk/ua
# https://generatefakename.com/ru/name/male/uk/ua
# https://generatefakename.com/ru/name/female/uk/ua

import requests
from bs4 import BeautifulSoup
import urllib3
import os

def get_page_content(url):
    try:
        response = requests.get(url, verify=False)
        response.raise_for_status()  # Проверка наличия ошибок HTTP
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при получении страницы: {e}")
        return None


# Отключаем предупреждения о проверке SSL-сертификата
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
path = os.getcwd()
urls = [("male", "https://generatefakename.com/ru/name/male/uk/ua"),
        ("female", "https://generatefakename.com/ru/name/female/uk/ua")]

limit = 500

for url in urls:
    name_data = []
    for _ in range(limit):
        page_content = get_page_content(url[1])
        if page_content:
            soup = BeautifulSoup(page_content, "lxml")
            target_block = soup.find("div", class_="label label-primary").find_next("h3")
            if target_block:
                fio = target_block.text.strip().split()
                if url[0] == 'female':
                    if fio[-1].endswith('вна'):
                        fio = fio[1]
                    else:
                        fio = fio[0]
                elif url[0] == 'male':
                    if fio[-1].endswith('вич'):
                        fio = fio[1]
                    else:
                        fio = fio[0]
                name_data.append(fio)

    name_data = sorted(set(name_data))
    with open(f"{path}/{url[0]}.txt", "w", encoding="utf-8") as f:
        f.write('\n'.join(name_data) + '\n')
        print("save data...")
