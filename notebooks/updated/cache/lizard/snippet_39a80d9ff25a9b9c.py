def load(source, **kwargs):
    with open(source, 'rb') as f:
        return torch.load(f, **kwargs)