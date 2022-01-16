import torch
from model import flower_model

dev = torch.device("cpu")
model = flower_model().to(dev)
model.load_state_dict(torch.load("model/flowers_cnn.ckpt", map_location=dev))
model.eval()

dummy = torch.zeros(1, 3, 112, 112)
torch.onnx.export(model, dummy, "model/flower_model.onnx", verbose=True)
