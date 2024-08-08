import os
import json
from jsonmerge import merge

json_dir = './Lua/luas'
output_file = './Lua/lua_lang.json'

merged_data = {}

for filename in os.listdir(json_dir):
    if filename.endswith('.json'):
        file_path = os.path.join(json_dir, filename)
        print(f'Merging {file_path}...')
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            merged_data = merge(merged_data, data)

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(merged_data, f, ensure_ascii=False, indent=4)

print(f'All JSON files in {json_dir} have been merged into {output_file}')
