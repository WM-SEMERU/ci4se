def delete_file_system(filesystemid, keyid=None, key=None, profile=None,
    region=None, **kwargs):
    client = _get_conn(key=key, keyid=keyid, profile=profile, region=region)
    client.delete_file_system(FileSystemId=filesystemid)