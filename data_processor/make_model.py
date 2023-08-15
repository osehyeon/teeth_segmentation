import torch
from torchvision.transforms import functional as F
from torch.utils.data import DataLoader, Dataset
from PIL import Image
import json
import os

class_labels = {
    "ortho": 0,
    "gcr": 1,
    "mcr": 2,
    "cecr": 3,
    "am" : 4,
    "zircr": 5,
    "tar1": 6, 
    "tar2": 7,
    "tar3": 8
}


class CustomDataset(Dataset):
    def __init__(self, img_dir, json_dir):
        self.img_dir = img_dir
        self.json_files = [f for f in os.listdir(json_dir) if f.endswith('.json')]
        self.json_dir = json_dir  # Add this line to store the JSON directory path

    def __len__(self):
        return len(self.json_files)

    def __getitem__(self, idx):
        json_file = os.path.join(self.json_dir, self.json_files[idx])
        with open(json_file, 'r') as f:
            data = json.load(f)
            img_path = os.path.join(self.img_dir, data['imagePath'])
            image = Image.open(img_path).convert("RGB")
            boxes = []
            labels = []
            for shape in data['shapes']:
                box = [point[0] for point in shape['points']] + [point[1] for point in shape['points']]
                boxes.append(box)
                
                # Get the shape's label from the JSON data
                shape_label = shape['label']
                class_label = class_labels.get(shape_label, -1)  # -1 if label not found
                labels.append(class_label)
            
            return F.to_tensor(image), {"boxes": torch.FloatTensor(boxes), "labels": torch.LongTensor(labels)}






img_dir = '../datasets/images/b057/'
json_dir = '../datasets/annotations/b057/'
dataset = CustomDataset(img_dir, json_dir)
dataloader = DataLoader(dataset, batch_size=2, shuffle=True, collate_fn=lambda x: tuple(zip(*x)))