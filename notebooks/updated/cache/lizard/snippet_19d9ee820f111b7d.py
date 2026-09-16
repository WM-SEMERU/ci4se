def from_file(cls, filename):
    yaml = YAML(typ='safe')
    with open(filename, 'r') as f:
        d = yaml.load(f)
    return cls.from_dict(d)