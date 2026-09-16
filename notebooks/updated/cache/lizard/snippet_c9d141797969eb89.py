def rm_files(path, extension):
    files = list_files(extension, path)
    for file in files:
        if file.endswith(extension):
            os.remove(os.path.join(path, file))
    return