import os
import shutil

def move_files_by_extension(src_dir, dest_dir, extension):
    for filename in os.listdir(src_dir):
        if filename.endswith(extension):
            shutil.move(os.path.join(src_dir, filename), os.path.join(dest_dir, filename))

# 원본 폴더
source_directory = '../datasets'  # 현재 경로로 설정

# jpg 파일 이동
move_files_by_extension(source_directory, '../datasets/images/', '.jpg')

# json 파일 이동
move_files_by_extension(source_directory, '../datasets/annotations/', '.json')