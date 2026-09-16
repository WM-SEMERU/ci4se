def dump_resource_to_zipfile(resource, zipfile, content_type=None):
    if content_type is None:
        content_type = CsvMime
    srl = ConnectedResourcesSerializer(content_type)
    srl.to_zipfile(resource, zipfile)