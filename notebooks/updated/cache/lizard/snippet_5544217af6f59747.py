def read_files(path):
    template = {}
    for file_name in os.listdir(path):
        with open(os.path.join(path, file_name), 'r') as f:
            template[file_name] = replace_whitespace(f.read(), insert=True)
    return template