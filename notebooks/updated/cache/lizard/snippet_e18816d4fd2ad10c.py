def load_manifest(app, filename='manifest.json'):
    if os.path.isabs(filename):
        path = filename
    else:
        path = pkg_resources.resource_filename(app, filename)
    with io.open(path, mode='r', encoding='utf8') as stream:
        data = json.load(stream)
    _registered_manifests[app] = path
    return data