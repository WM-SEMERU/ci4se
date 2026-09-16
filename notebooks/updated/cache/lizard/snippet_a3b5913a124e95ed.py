def download(url, filename, overwrite=False):
    from requests import get
    from os.path import exists
    debug('Downloading ' + unicode(url) + '...')
    data = get(url)
    if data.status_code == 200:
        if not exists(filename) or overwrite:
            f = open(filename, 'wb')
            f.write(data.content)
            f.close()
        return True
    return False