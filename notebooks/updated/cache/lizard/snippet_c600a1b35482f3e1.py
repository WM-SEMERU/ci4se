def find_dotenv(filename='.env', raise_error_if_not_found=False, usecwd=False):
    if usecwd or '__file__' not in globals():
        path = os.getcwd()
    else:
        frame_filename = sys._getframe().f_back.f_code.co_filename
        path = os.path.dirname(os.path.abspath(frame_filename))
    for dirname in _walk_to_root(path):
        check_path = os.path.join(dirname, filename)
        if os.path.exists(check_path):
            return check_path
    if raise_error_if_not_found:
        raise IOError('File not found')
    return ''