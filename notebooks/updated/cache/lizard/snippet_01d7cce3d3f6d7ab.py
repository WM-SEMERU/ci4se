def do_ams_sto_put(endpoint, body, content_length):
    headers = {'Accept': json_acceptformat, 'Accept-Charset': charset,
        'x-ms-blob-type': 'BlockBlob', 'x-ms-meta-m1': 'v1', 'x-ms-meta-m2':
        'v2', 'x-ms-version': '2015-02-21', 'Content-Length': str(
        content_length)}
    return requests.put(endpoint, data=body, headers=headers)