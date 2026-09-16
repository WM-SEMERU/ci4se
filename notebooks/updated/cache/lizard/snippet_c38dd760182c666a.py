def unzip_data():
    with ZipFile(os.path.join(CACHE_FOLDER, CACHE_ZIP), 'r') as zf:
        zf.extractall(path=CACHE_FOLDER)