def directory_files(path):
    for entry in os.scandir(path):
        if not entry.name.startswith('.') and entry.is_file():
            yield entry.name