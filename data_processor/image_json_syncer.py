import os
import shutil

# 이미지와 json 파일의 기본 경로 설정
image_path = '../datasets/images/'
ids = ['091', 'a091', 'b057', 'c031']

for identifier in ids:
    current_annotation_folder = '../datasets/annotations/' + identifier + '/'

    for json_file in os.listdir(current_annotation_folder):
        # json 파일만 처리
        if json_file.endswith('.json'):
            # json 파일 이름에서 '_식별번호' 부분을 제거해 이미지 이름 추출
            image_name = json_file.rsplit('_', 1)[0] + '.jpg'
            
            source_image_path = os.path.join(image_path, image_name)
            destination_folder = os.path.join(image_path, identifier)
            
            # 식별번호에 해당하는 폴더가 없다면 생성
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)

            destination_image_path = os.path.join(destination_folder, image_name)
            
            # 이미지 파일을 해당 폴더로 복사
            shutil.copy(source_image_path, destination_image_path)

print("작업 완료!")