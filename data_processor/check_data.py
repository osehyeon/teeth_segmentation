import os

folder_path = '../datasets/b057/'  # 여기에 폴더 경로를 입력하세요.

# JSON과 PNG 파일 개수 확인
json_files_count = sum(1 for f in os.listdir(folder_path) if f.endswith('.json'))
png_files_count = sum(1 for f in os.listdir(folder_path) if f.endswith('.jpg'))

print(f"Number of JSON files: {json_files_count}")
print(f"Number of jpg files: {png_files_count}")
