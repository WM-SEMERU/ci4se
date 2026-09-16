def load(cls, path):
    with open(path, 'r') as in_file:
        metadata = json.load(in_file)
    return cls.from_dict(metadata)