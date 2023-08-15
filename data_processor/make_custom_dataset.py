import os
import json
import cv2
import numpy as np
import torch
from torch.utils.data import Dataset, DataLoader

class CustomDataset:
    def __init__(self, json_directory):
        self.json_directory = json_directory
        self.data = []

        self._load_data()

    def _load_data(self):
        index = 0
        for json_file in os.listdir(self.json_directory):
            full_json_path = os.path.join(self.json_directory, json_file)
            if json_file.endswith('.json'):
                with open(full_json_path, 'r') as f:
                    json_data = json.load(f)
                
                image_path = os.path.join(self.json_directory, json_data["imagePath"])
                
                # Ensure the image file exists
                if not os.path.exists(image_path):
                    print(f"Image file {image_path} does not exist. Deleting the JSON data in {json_file}.")
                    os.remove(full_json_path)
                    continue
                
                polygons = [shape["points"] for shape in json_data["shapes"]]
                labels = [shape["label"] for shape in json_data["shapes"]]
                
                self.data.append({
                    "image_path": image_path,
                    "polygons": polygons,
                    "labels": labels
                })

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        data_item = self.data[idx]
        image = cv2.imread(data_item["image_path"])  # BGR format
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB
        
        polygons = data_item["polygons"]
        labels = data_item["labels"]
        
        return image, polygons, labels

# Example usage
dataset_directory = "../datasets/b057/"
dataset = CustomDataset(dataset_directory)

image, polygons, labels = dataset[0]

data = [] 
for a, b, c in dataset:
    for i in c: 
        if i not in data:
            data.append(i)

print(data)

class_labels = {
    "ortho": 0,
    "gcr": 1,
    "mcr": 2,
    "cecr": 3,
    "am": 4,
    "tar1": 5,
    "tar2": 6,
    "tar3": 7
}