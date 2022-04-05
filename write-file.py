import json
import sys
import os.path

file_path = './localization.json'

data = {}
en = sys.argv[1]
ko = sys.argv[2]

if os.path.exists(file_path):
  with open(file_path, 'r', encoding='utf-8') as json_data:
    data = json.load(json_data)
else:
  with open(file_path, 'w', encoding='utf-8') as out:
    data = { 'en': [], 'ko': [] }
    json.dump(data, out, indent=2)

data['en'].append({ 'text': en })
data['ko'].append({ 'text': ko })

with open(file_path, 'w', encoding='utf-8') as json_out:
  json.dump(data, json_out, indent=2, ensure_ascii=False)

print('success')
