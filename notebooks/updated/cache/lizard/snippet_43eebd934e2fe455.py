def load_all_yamls(cls, directories):
    yaml_files = []
    loaded_yamls = {}
    for d in directories:
        if d.startswith('/home') and not os.path.exists(d):
            os.makedirs(d)
        for dirname, subdirs, files in os.walk(d):
            yaml_files.extend(map(lambda x: os.path.join(dirname, x),
                filter(lambda x: x.endswith('.yaml'), files)))
    for f in yaml_files:
        loaded_yamls[f] = cls.load_yaml_by_path(f)
    return loaded_yamls