import torch.nn as nn

class ResidualBlock(nn.Module):
    def _init_(self, in_channels, out_channels, stride=1):
        super()._init_()
        self.conv1 = nn.Conv2d(in_channels, out_channels,
                               3, stride, padding=1, bias=False)
        self.bn1 = nn.BatchNorm2d(out_channels)
        self.conv2 = nn.Conv2d(out_channels, out_channels, 
                               3, stride, padding=1, bias=False)