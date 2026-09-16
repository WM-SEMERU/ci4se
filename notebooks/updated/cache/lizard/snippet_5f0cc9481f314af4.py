def read_json_file(cls, path):
    with open(path, 'r') as f:
        return cls.from_dict(json.load(f))