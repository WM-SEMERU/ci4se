def load_json(file, new_root_dir=None, decompression=False):
    if decompression:
        with open(file, 'rb') as f:
            my_object = load(f, decompression=decompression)
    else:
        with open(file, 'r') as f:
            my_object = load(f, decompression=decompression)
    if new_root_dir:
        my_object.root_dir = new_root_dir
    return my_object