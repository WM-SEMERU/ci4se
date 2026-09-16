def download_url(url, destination):
    from settings import VALID_IMAGE_EXTENSIONS
    base_name, ext = os.path.splitext(url)
    ext = ext.lstrip('.')
    if ext not in VALID_IMAGE_EXTENSIONS:
        raise Exception('Invalid image extension')
    base_path, filename = os.path.split(destination)
    os.makedirs(base_path)
    urllib.urlretrieve(url, destination)