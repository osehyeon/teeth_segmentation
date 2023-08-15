import json
import os
import shutil
import random

# 원본 데이터의 경로
src_dir = '../datasets/annotations/c031/'

# Train 및 Test 폴더 경로
train_dir = src_dir + '/train/'
test_dir = src_dir + '/test/'

# 분할 비율 설정 (e.g., 80% 학습, 20% 테스트)
split_ratio = 0.8

# 경로에서 json 파일만 필터링
json_files = [f for f in os.listdir(src_dir) if f.endswith('.json')]

# 데이터를 무작위로 섞음
random.shuffle(json_files)

# Train과 Test로 나누기
num_train = int(len(json_files) * split_ratio)
train_files = json_files[:num_train]
test_files = json_files[num_train:]

# Train 및 Test 디렉토리 생성
os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# 파일을 해당 폴더로 복사
for file in train_files:
    # JSON 파일 복사
    shutil.copy(os.path.join(src_dir, file), train_dir)

    # JSON 파일에서 이미지 경로 찾기
    with open(os.path.join(src_dir, file), 'r') as jf:
        data = json.load(jf)
        image_file = data["imagePath"]

    # 이미지 파일 복사
    shutil.copy(os.path.join(src_dir, image_file), train_dir)

for file in test_files:
    # JSON 파일 복사
    shutil.copy(os.path.join(src_dir, file), test_dir)

    # JSON 파일에서 이미지 경로 찾기
    with open(os.path.join(src_dir, file), 'r') as jf:
        data = json.load(jf)
        image_file = data["imagePath"]

    # 이미지 파일 복사
    shutil.copy(os.path.join(src_dir, image_file), test_dir)