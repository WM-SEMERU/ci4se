def parser_from_buffer(cls, fp):
    yaml = YAML(typ='safe')
    return cls(yaml.load(fp))