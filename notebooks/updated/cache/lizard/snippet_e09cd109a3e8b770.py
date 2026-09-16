def get_tags(filesystemid, keyid=None, key=None, profile=None, region=None,
    **kwargs):
    client = _get_conn(key=key, keyid=keyid, profile=profile, region=region)
    response = client.describe_tags(FileSystemId=filesystemid)
    result = response['Tags']
    while 'NextMarker' in response:
        response = client.describe_tags(FileSystemId=filesystemid, Marker=
            response['NextMarker'])
        result.extend(response['Tags'])
    return result