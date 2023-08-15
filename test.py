import os
import shutil

# 이미지와 json 파일의 기본 경로 설정
image_path = '../datasetsimages/'

id = ['091/', 'a091/', 'b057/', 'c031/']

for i in id: 
    annotation_path = '../datasets/annotations/' + i
    print(annotation_path)