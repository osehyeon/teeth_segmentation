import torch
from torchvision.transforms import functional as F
from torch.utils.data import DataLoader, Dataset
from PIL import Image
import json
import os

class CustomDataset(Dataset):
    def __init__(self, img_dir, json_dir):
        self.img_dir = img_dir
        self.json_files = [f for f in os.listdir(json_dir) if f.endswith('.json')]

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
                labels.append(1)  # 예시로 1을 사용. 실제 클래스를 정의해야 함.
            return F.to_tensor(image), {"boxes": torch.FloatTensor(boxes), "labels": torch.LongTensor(labels)}

img_dir = '../datasets/images/b057/'
json_dir = '../datasets/annotations/b057/'
dataset = CustomDataset(img_dir, json_dir)
dataloader = DataLoader(dataset, batch_size=2, shuffle=True, collate_fn=lambda x: tuple(zip(*x)))