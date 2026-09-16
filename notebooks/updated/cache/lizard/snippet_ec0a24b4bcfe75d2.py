def delete_tags(filesystemid, tags, keyid=None, key=None, profile=None,
    region=None, **kwargs):
    client = _get_conn(key=key, keyid=keyid, profile=profile, region=region)
    client.delete_tags(FileSystemId=filesystemid, Tags=tags)