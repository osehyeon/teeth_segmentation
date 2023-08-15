import os
import json
import shutil

# 폴더 경로 지정
annotations_folder = "../datasets/annotations/c031"
images_folder = "../datasets/images"

# 지정된 폴더에서 모든 json 파일을 가져옴
json_files = [f for f in os.listdir(annotations_folder) if f.endswith('.json')]

for json_file in json_files:
    json_path = os.path.join(annotations_folder, json_file)
    
    # json 파일을 읽어서 imagePath 값을 가져옴
    with open(json_path, 'r') as f:
        data = json.load(f)
        image_name = data['imagePath']
    
    # 원래 이미지의 경로와 복사될 경로를 지정
    source_image_path = os.path.join(images_folder, image_name)
    target_image_path = os.path.join(annotations_folder, image_name)
    
    # 원본 이미지가 존재하는지 확인
    if os.path.exists(source_image_path):
        # 이미지를 annotations 폴더로 복사
        shutil.copy2(source_image_path, target_image_path)
    else:
        # 원본 이미지가 존재하지 않으면 json 파일 삭제
        os.remove(json_path)
        print(f"Deleted {json_file} because the image {image_name} doesn't exist.")

print("Operation completed.")