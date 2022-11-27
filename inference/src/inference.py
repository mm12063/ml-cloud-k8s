from __future__ import print_function
import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import datasets, transforms
from os.path import exists

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, 3, 1)
        self.conv2 = nn.Conv2d(32, 64, 3, 1)
        self.dropout1 = nn.Dropout(0.25)
        self.dropout2 = nn.Dropout(0.5)
        self.fc1 = nn.Linear(9216, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = self.conv1(x)
        x = F.relu(x)
        x = self.conv2(x)
        x = F.relu(x)
        x = F.max_pool2d(x, 2)
        x = self.dropout1(x)
        x = torch.flatten(x, 1)
        x = self.fc1(x)
        x = F.relu(x)
        x = self.dropout2(x)
        x = self.fc2(x)
        output = F.log_softmax(x, dim=1)
        return output

def get_inference(num_to_predict):
    actuals, preds, errs = [], [], []

    test_kwargs = {'batch_size':100,
                   'shuffle': True}

    transform=transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
        ])

    loc = "/home/app/data"
    if exists(loc):
        dataset = datasets.MNIST(loc, download=True, train=False, transform=transform)
        test_loader = torch.utils.data.DataLoader(dataset, **test_kwargs)

        PATH = "/home/app/mnist_model/model.pt"
        if exists(PATH):
            model = Net()
            model.load_state_dict(torch.load(PATH))
            model.eval()

            images, labels = next(iter(test_loader))
            actuals = labels[:num_to_predict].numpy()

            test_output = model(images[:num_to_predict])
            preds = torch.max(test_output, 1)[1].data.numpy().squeeze()
        else:
            errs.append(f"Can't find dir: {PATH}")
    else:
        errs.append(f"Can't find dir: {loc}")

    return actuals, preds, errs
















#
# if __name__ == '__main__':
#     main()