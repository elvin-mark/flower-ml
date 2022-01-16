from flask import Flask, render_template, request
import pickle
import torch
import torch.nn as nn
import torchvision
from model import flower_model
import PIL
from PIL import Image
import base64
from io import BytesIO
import json


app = Flask(__name__)

dev = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

with open("data/flower_labels.pkl", "rb") as f:
    labels_ = pickle.load(f)

model = flower_model().to(dev)
model.load_state_dict(torch.load("model/flowers_cnn.ckpt", map_location=dev))
model.eval()

test_transform = torchvision.transforms.Compose([
    torchvision.transforms.Resize((112, 112)),
    torchvision.transforms.ToTensor(),
    torchvision.transforms.Normalize([0.49139968, 0.48215827, 0.44653124], [
        0.24703233, 0.24348505, 0.26158768])
])

softmax = nn.Softmax(dim=1)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/flower", methods=["POST"])
def flower():
    response = {"predictions": []}
    if request.method == "POST":
        data = request.json["img"]
        img = BytesIO(base64.b64decode(data[23:]))
        img = Image.open(img)
        x = test_transform(img).reshape((1, -1, 112, 112))
        prob = 100*softmax(model(x.to(dev)))[0]
        pred = torch.argsort(prob, descending=True)[:5]
        response = {"predictions": [
            {"prob": p.item(), "name": labels_[i]} for i, p in zip(pred, prob[pred])]}
        print(response)
    return json.dumps(response)


if __name__ == "__main__":
    app.run()
