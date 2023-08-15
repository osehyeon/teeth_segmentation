import os

def move_json_to_identified_folders(directory):
    all_files = os.listdir(directory)
    
    json_files = [f for f in all_files if f.endswith('.json')]

    for json_file in json_files:
        # 식별 번호 추출
        identifier = json_file.rsplit('_', 1)[-1].replace('.json', '')
        
        # 해당 식별 번호로 폴더 생성
        target_folder = os.path.join(directory, identifier)
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)
        
        # json 파일을 해당 폴더로 이동
        os.rename(os.path.join(directory, json_file), os.path.join(target_folder, json_file))

source_directory = '../datasets/annotations'  # 현재 경로로 설정
move_json_to_identified_folders(source_directory)