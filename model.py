import torch
import torch.nn as nn


def simple_conv_block(in_planes, out_planes, kernel_size, stride=1, padding=0):
    return nn.Sequential(
        nn.Conv2d(in_planes, out_planes, kernel_size=kernel_size,
                  stride=stride, padding=padding, bias=False),
        nn.BatchNorm2d(out_planes),
        nn.ReLU(inplace=True),
        nn.MaxPool2d(kernel_size=2)
    )


def flower_model(num_classes=102):
    return nn.Sequential(
        simple_conv_block(3, 32, 3),
        simple_conv_block(32, 32, 3),
        simple_conv_block(32, 64, 3),
        simple_conv_block(64, 64, 3),
        simple_conv_block(64, 128, 3),
        nn.Flatten(),
        nn.Linear(128, num_classes)
    )
