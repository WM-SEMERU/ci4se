def read_key_value_pairs_from_file(*path):
    with open(os.path.join(*path)) as f:
        for line in f:
            yield line.split(' ', 1)