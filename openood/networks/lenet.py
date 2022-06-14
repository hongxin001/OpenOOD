import logging

import torch.nn as nn

logger = logging.getLogger(__name__)


class LeNet(nn.Module):
    def __init__(self, num_classes, num_channel=3):
        super(LeNet, self).__init__()
        self.num_classes = num_classes
        self.feature_size = 120
        self.block1 = nn.Sequential(
            nn.Conv2d(in_channels=num_channel,
                      out_channels=6,
                      kernel_size=5,
                      stride=1,
                      padding=2), nn.ReLU(), nn.MaxPool2d(kernel_size=2))

        self.block2 = nn.Sequential(
            nn.Conv2d(in_channels=6, out_channels=16, kernel_size=5, stride=1),
            nn.ReLU(), nn.MaxPool2d(kernel_size=2))

        self.block3 = nn.Sequential(
            nn.Conv2d(in_channels=16,
                      out_channels=120,
                      kernel_size=5,
                      stride=1), nn.ReLU())

        self.classifier1 = nn.Linear(in_features=120, out_features=84)
        self.relu = nn.ReLU()
        self.fc = nn.Linear(in_features=84, out_features=num_classes)
        self.feature_size = 84

    def get_fc(self):
        fc = self.fc
        return fc.weight.cpu().detach().numpy(), fc.bias.cpu().detach().numpy()

    def forward(self,
                x,
                return_feature=False,
                return_feature_list=False,
                forward_secondary=True):
        if forward_secondary:
            return self.forward_secondary(x, return_feature,
                                          return_feature_list)
        else:
            feature1 = self.block1(x)
            feature2 = self.block2(feature1)
            feature3 = self.block3(feature2)
            feature = feature3.view(feature3.shape[0], -1)
            logits_cls = self.fc(self.relu(self.classifier1(feature)))
            feature_list = [feature1, feature2, feature3]
            if return_feature:
                return logits_cls, feature
            elif return_feature_list:
                return logits_cls, feature_list
            else:
                return logits_cls

    def forward_secondary(self,
                          x,
                          return_feature=False,
                          return_feature_list=False):
        feature1 = self.block1(x)
        feature2 = self.block2(feature1)
        feature3 = self.block3(feature2)
        feature3 = feature3.view(feature3.shape[0], -1)
        feature4 = self.classifier1(feature3)
        feature = feature4.view(feature4.shape[0], -1)
        logits_cls = self.fc(self.relu(feature))
        feature_list = [feature1, feature2, feature3, feature4]
        if return_feature:
            return logits_cls, feature
        elif return_feature_list:
            return logits_cls, feature_list
        else:
            return logits_cls