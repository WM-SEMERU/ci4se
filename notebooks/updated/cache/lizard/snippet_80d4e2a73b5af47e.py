def unpack_epub(file, directory):
    if zipfile.is_zipfile(file):
        with zipfile.ZipFile(file, 'r') as zf:
            zf.extractall(path=directory)