def replace_py_ipynb(fname):
    fname_prefix, extension = os.path.splitext(fname)
    allowed_extension = '.py'
    if extension != allowed_extension:
        raise ValueError('Unrecognized file extension, expected %s, got %s' %
            (allowed_extension, extension))
    new_extension = '.ipynb'
    return '{}{}'.format(fname_prefix, new_extension)