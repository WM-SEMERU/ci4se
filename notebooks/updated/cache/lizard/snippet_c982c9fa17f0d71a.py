def get_temp_dir(suffix=None):
    to_join = [tempfile.gettempdir()]
    if os.name == 'nt':
        to_join.append('spyder')
    else:
        username = encoding.to_unicode_from_fs(getuser())
        to_join.append('spyder-' + username)
    if suffix is not None:
        to_join.append(suffix)
    tempdir = osp.join(*to_join)
    if not osp.isdir(tempdir):
        os.mkdir(tempdir)
    return tempdir