def from_url(cls, url, **kwargs):
    username = kwargs.get('username')
    password = kwargs.get('password')
    headers = kwargs.get('headers', {})
    auth = None
    path = kwargs.get('path', '/tmp/app.zip')
    dest = kwargs.get('dest', '/app')
    if username and password:
        auth = base64.b64encode(b'%s:%s' % (username, password))
    if auth:
        headers['Authorization'] = 'Basic %s' % auth.decode('utf8')
    r = request.get(url, headers=headers, stream=True)
    if r.status_code != 200:
        err_msg = 'Could not download resource from url (%s): %s'
        err_args = r.status_code, url
        raise errors.DownloadError(err_msg % err_args)
    with open('/tmp/app.zip', 'wb+') as f:
        chunks = r.iter_content(chunk_size=1024)
        [f.write(chunk) for chunk in chunks if chunk]
    return cls.from_zip(path, dest)