import json

# JSON 파일들이 저장된 폴더의 경로
json_file_path = '../datasets/trainvals/trainval_c031.json'  # 여기에 실제 경로를 입력하세요.


# JSON 파일 읽기
with open(json_file_path, 'r') as jf:
    data = json.load(jf)
    category_ids = [item["category_id"] for item in data["annotations"]]

# 고유한 category_id 값의 개수 계산
unique_category_ids_count = len(set(category_ids))

print(f"Number of unique labels (category_ids): {unique_category_ids_count}")
