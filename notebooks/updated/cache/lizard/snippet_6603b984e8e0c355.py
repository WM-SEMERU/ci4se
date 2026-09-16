def get_metadata_path(name):
    return pkg_resources.resource_filename('voobly', os.path.join(
        METADATA_PATH, '{}.json'.format(name)))