import torch
from model import FootprintModel

def train():
    print("Footprint training start")

    model = FootprintModel()
    print(model)

if __name__ == "__main__":
    train()
