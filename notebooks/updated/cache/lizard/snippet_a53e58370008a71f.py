def is_jar(path):
    if os.path.isfile(path) and zipfile.is_zipfile(path):
        try:
            with zipfile.ZipFile(path) as f:
                if 'META-INF/MANIFEST.MF' in f.namelist():
                    return True
        except (IOError, zipfile.BadZipfile):
            pass
    return False