import os
import json

class_labels = {
    "ortho": 0,
    "gcr": 1,
    "mcr": 2,
    "cecr": 3,
    "am": 4,
    "zircr": 5,
    "tar1": 6,
    "tar2": 7,
    "tar3": 8
}

json_dir = "../datasets/annotations/b057"  # JSON 파일들이 저장된 디렉토리 경로
image_dir = "../datasets/images/b057/"  # 이미지 파일들이 저장된 디렉토리 경로

for json_file in os.listdir(json_dir):
    if json_file.endswith(".json"):
        json_path = os.path.join(json_dir, json_file)
        
        with open(json_path, "r") as f:
            data = json.load(f)
            
        shapes = data.get("shapes", [])
        keep_file = False
        mismatched_labels = []
        
        for shape in shapes:
            if "label" in shape and shape["label"] in class_labels:
                keep_file = True
            else:
                mismatched_label = shape.get("label")
                if mismatched_label:
                    mismatched_labels.append(mismatched_label)
        
        if not keep_file:
            print(f"Deleting {json_file}")
            os.remove(json_path)
            for label in mismatched_labels:
                print(f"Mismatched label in {json_file}: {label}")
            
            # Deleting associated image file
            image_filename = data.get("imagePath", "")
            image_path = os.path.join(image_dir, image_filename)
            if os.path.exists(image_path):
                os.remove(image_path)
                print(f"Deleted associated image file: {image_filename}")
        else:
            print(f"Keeping {json_file}")