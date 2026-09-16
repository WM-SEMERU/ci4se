def pyc_to_py(path_to_file):
    stem, ext = os.path.splitext(path_to_file)
    if ext == '.pyc':
        return '%s.py' % stem
    return path_to_file