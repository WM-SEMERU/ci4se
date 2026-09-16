def frame_unique(f):
    return f.f_code.co_filename, f.f_code.co_name, f.f_lineno