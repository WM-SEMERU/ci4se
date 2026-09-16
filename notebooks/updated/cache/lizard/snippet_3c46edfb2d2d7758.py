def openSafeReplace(filepath, mode='w+b'):
    tempfileName = None
    if not _isFileAccessible(filepath):
        raise IOError('File %s is not writtable' % (filepath,))
    with tempfile.NamedTemporaryFile(delete=False, mode=mode) as tmpf:
        tempfileName = tmpf.name
        yield tmpf
    if not _isFileAccessible(filepath):
        raise IOError('File %s is not writtable' % (filepath,))
    shutil.move(tempfileName, filepath)