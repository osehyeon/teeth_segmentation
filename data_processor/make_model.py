import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision.models.segmentation import deeplabv3_resnet50
from torchvision.datasets import CocoDetection
from torchvision.transforms import functional as F
from torchvision import transforms
from pycocotools.coco import COCO
import os 
from PIL import Image, ImageDraw


# COCO 형식 데이터셋 로드 및 전처리
class CustomCOCO(CocoDetection):
    def __init__(self, root, annFile, transform=None):
        super(CustomCOCO, self).__init__(root, annFile)
        self.coco = COCO(annFile)
        self.ids = list(sorted(self.coco.imgs.keys()))

    def __getitem__(self, index):
        coco = self.coco
        img_id = self.ids[index]
        ann_ids = coco.getAnnIds(imgIds=img_id)
        target = coco.loadAnns(ann_ids)
        
        path = coco.loadImgs(img_id)[0]['file_name']
        img = F.pil_to_tensor(Image.open(os.path.join(self.root, path)).convert('RGB')).float().div(255)

        masks = []
        for ann in target:
            poly = ann['segmentation'][0]
            nx = len(poly) // 2
            x, y = poly[:nx], poly[nx:]
            mask = Image.new("L", (img.shape[2], img.shape[1]))
            ImageDraw.Draw(mask).polygon(list(zip(x, y)), fill=1)
            masks.append(F.pil_to_tensor(mask))
        masks = torch.stack(masks).sum(0)
        
        if self.transform:
            img = self.transform(img)
            
        return img, masks

transform = transforms.Compose([
    transforms.ToPILImage(),
    transforms.Resize((256, 256)),
    transforms.ToTensor()
])

dataset = CustomCOCO(root="../datasets/images/", annFile="../datasets/trainvals/trainval_c031.json", transform=transform)
dataloader = DataLoader(dataset, batch_size=8, shuffle=True)

# 모델, 옵티마이저 설정
model = deeplabv3_resnet50(pretrained=False, num_classes=38)
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)
optimizer = optim.Adam(model.parameters(), lr=0.0001)

# 학습 루프
num_epochs = 10
for epoch in range(num_epochs):
    model.train()
    for i, (imgs, masks) in enumerate(dataloader):
        imgs, masks = imgs.to(device), masks.to(device).long()
        
        optimizer.zero_grad()
        output = model(imgs)['out']
        loss = nn.CrossEntropyLoss()(output, masks.squeeze(1))
        loss.backward()
        optimizer.step()

        if i % 10 == 0:
            print(f"Epoch: {epoch}/{num_epochs}, Batch: {i}/{len(dataloader)}, Loss: {loss.item()}")

# 모델 저장
torch.save(model.state_dict(), "segmentation_model.pth")
