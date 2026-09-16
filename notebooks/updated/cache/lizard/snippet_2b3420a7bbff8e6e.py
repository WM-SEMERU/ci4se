def abs_path(rel_path):
    return os.path.abspath(os.path.join(os.path.dirname(sys._getframe(1).
        f_code.co_filename), rel_path))