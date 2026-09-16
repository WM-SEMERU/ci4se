def load(cls, file_path):
    data = helper.read_json(file_path)
    return ConciseCV.from_dict(data)