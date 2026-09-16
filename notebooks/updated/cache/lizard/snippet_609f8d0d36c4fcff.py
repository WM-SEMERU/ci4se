def extract_metadata(fileobj):
    tar = tarfile.open(mode='r:gz', fileobj=fileobj)
    plugin_path = path(tmp.mkdtemp(prefix='mpm-'))
    try:
        tar.extractall(plugin_path)
        return yaml.load(plugin_path.joinpath('properties.yml').bytes())
    finally:
        fileobj.seek(0)
        plugin_path.rmtree()