def write_config_file(path, config):
    contents = json.dumps(config, indent=4, separators=(',', ': ')) + '\n'
    try:
        with open(path, 'w') as f:
            f.write(contents)
        return True
    except IOError as ex:
        if ex != errno.ENOENT:
            raise
    return False