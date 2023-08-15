import os

def paired_files(directory):
    # 모든 파일 리스트 가져오기
    all_files = os.listdir(directory)
    
    jpg_files = [f for f in all_files if f.endswith('.jpg')]
    json_files = [f for f in all_files if f.endswith('.json')]

    jpg_basenames = [os.path.splitext(f)[0] for f in jpg_files]

    # 각 jpg 파일에 대해 짝이 되는 json 파일이 있는지 확인
    for jpg_base in jpg_basenames:
        matching_jsons = [f for f in json_files if f.startswith(jpg_base)]
        
        # 매칭되는 json 파일이 없다면 jpg 파일 삭제
        if not matching_jsons:
            os.remove(os.path.join(directory, jpg_base + '.jpg'))
            print(f"Deleted: {jpg_base}.jpg")

    # json 파일 중 jpg 파일과 매칭되지 않는 것은 삭제
    for json_file in json_files:
        base_without_suffix = os.path.splitext(json_file)[0].rsplit('_', 1)[0]
        if base_without_suffix not in jpg_basenames:
            os.remove(os.path.join(directory, json_file))
            print(f"Deleted: {json_file}")

source_directory = '../datasets'  # 현재 경로로 설정
paired_files(source_directory)