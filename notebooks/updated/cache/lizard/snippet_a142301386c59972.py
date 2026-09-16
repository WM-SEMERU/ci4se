def copy(src, dst):
    assert isinstance(src, str)
    assert os.path.exists(src)
    assert isinstance(dst, str)
    abs_path = os.path.dirname(os.path.abspath(dst))
    if not os.path.isdir(abs_path):
        os.makedirs(abs_path)
    if os.path.isfile(src):
        shutil.copy(src, dst)
    elif os.path.isdir(src):
        shutil.copytree(src, dst)
    else:
        raise ValueError('Unsupported file: {}'.format(src))
    chmod(dst)