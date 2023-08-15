import os
import json

def process_json_files(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            json_path = os.path.join(folder_path, filename)
            with open(json_path, "r") as json_file:
                json_data = json.load(json_file)
            
            if json_data.get("imageData") is None or json_data.get("imagePath") is None or json_data.get("shapes") is None:
                os.remove(json_path)
                print(f"Deleted {filename}")

# Replace 'folder_path' with the actual path of your folder containing JSON files
folder_path = "../datasets/annotations/c031/"
process_json_files(folder_path)