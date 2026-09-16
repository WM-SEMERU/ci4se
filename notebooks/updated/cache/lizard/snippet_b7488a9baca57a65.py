def get_metadata(item):
    for metadata_key in ('METADATA', 'PKG-INFO'):
        try:
            metadata_lines = item.get_metadata_lines(metadata_key)
            break
        except (KeyError, IOError):
            metadata_lines = []
    return metadata_lines