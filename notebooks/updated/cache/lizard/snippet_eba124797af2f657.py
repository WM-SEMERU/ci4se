def load_yaml_file(file):
    if not hasattr(file, 'read'):
        with io.open(file, 'r', encoding='utf-8') as f:
            return yaml.load(f, yaml.FullLoader)
    return yaml.load(file, yaml.FullLoader)