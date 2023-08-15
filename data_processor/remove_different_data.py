import os
import json

folder_path = '../datasets/b057/'

# 모든 JSON 파일 확인
json_files = [f for f in os.listdir(folder_path) if f.endswith('.json')]
jpg_files = set(f for f in os.listdir(folder_path) if f.endswith('.jpg'))

# JSON 파일의 imagePath로 JPG 파일 확인
for json_file in json_files:
    full_json_path = os.path.join(folder_path, json_file)
    with open(full_json_path, 'r') as f:
        data = json.load(f)
    
    image_path = data.get("imagePath", "")
    
    if image_path not in jpg_files:
        os.remove(full_json_path)
        print(f"Deleted JSON file: {json_file}")
    else:
        jpg_files.remove(image_path)

# 남은 JPG 파일 삭제
for jpg_file in jpg_files:
    os.remove(os.path.join(folder_path, jpg_file))
    print(f"Deleted JPG file: {jpg_file}")s