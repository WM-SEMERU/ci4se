def _find_files(directory):
    pattern = '{directory}/*.xml'.format(directory=directory)
    files = glob(pattern)
    return files