# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests
import json
from bs4 import BeautifulSoup


group_id = '164472558'
group_name = 'proxysocks5'
url = f"https://vk.com/{group_name}?w=wall-{group_id}_"
headers = {'accept': '*/*', 'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
     (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
result = []

response = requests.get(url, headers=headers)
html = response.text
soup = BeautifulSoup(html, 'lxml')
post_texts = soup.find_all(class_="wall_post_text")

for post_text in post_texts:
    for br in post_text.find_all(name='br'):
        br.replace_with('\n')
    text = post_text.get_text().strip()
    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        if ':' in line:
            result.append(line)

json_result = json.dumps(result, ensure_ascii=False)
with open('result.txt', 'w') as txt_file:
    for item in result:
        txt_file.write(item + '\n')

# Сохранение в файл формата JSON
with open('result.json', 'w') as json_file:
    json.dump(result, json_file, ensure_ascii=False)


