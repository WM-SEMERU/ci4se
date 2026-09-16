def DownloadResource(url, path):
    import requests
    from six import BytesIO
    import zipfile
    print('Downloading... {} to {}'.format(url, path))
    r = requests.get(url, stream=True)
    z = zipfile.ZipFile(BytesIO(r.content))
    z.extractall(path)
    print('Completed download and extraction.')