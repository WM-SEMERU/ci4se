def save(cls, filename, config):
    mode = os.O_WRONLY | os.O_TRUNC | os.O_CREAT
    with os.fdopen(os.open(filename, mode, 384), 'w') as fname:
        yaml.safe_dump(config, fname, indent=4, default_flow_style=False)