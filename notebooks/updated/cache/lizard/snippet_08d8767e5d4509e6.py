def dump_resource_to_files(resource, content_type=None, directory=None):
    if directory is None:
        directory = os.getcwd()
    if content_type is None:
        content_type = CsvMime
    srl = ConnectedResourcesSerializer(content_type)
    srl.to_files(resource, directory=directory)