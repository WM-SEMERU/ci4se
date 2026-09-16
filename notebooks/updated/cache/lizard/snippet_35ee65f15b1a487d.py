def _load(cls, path):
    bytesIO = BytesIO()
    initfile = os.path.join(path, '__init__.py')
    if os.path.isfile(initfile):
        rootDir = os.path.dirname(path)
    else:
        rootDir = path
    with ZipFile(file=bytesIO, mode='w') as zipFile:
        for dirName, _, fileList in os.walk(path):
            for fileName in fileList:
                fullPath = os.path.join(dirName, fileName)
                zipFile.write(fullPath, os.path.relpath(fullPath, rootDir))
    bytesIO.seek(0)
    return bytesIO