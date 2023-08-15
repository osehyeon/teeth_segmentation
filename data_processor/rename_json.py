import os 

ids = ['a091', 'b057', 'c031']

for id in ids: 
    folder_path = '../datasets/annotations/' + id + '/'

    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            name_parts = filename.rsplit('_', 1)  # 오른쪽부터 첫 번째 '_'를 기준으로 분리
            if len(name_parts) > 1:
                new_filename = f"{name_parts[0]}.json"
                original_file_path = os.path.join(folder_path, filename)
                new_file_path = os.path.join(folder_path, new_filename)
                
                # 파일 이름을 변경합니다.
                os.rename(original_file_path, new_file_path)
                print(f'Renamed: {filename} -> {new_filename}')