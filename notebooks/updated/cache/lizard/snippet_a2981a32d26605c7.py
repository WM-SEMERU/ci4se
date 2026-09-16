def _path_to_module(path):
    path = 'rapport' + path.split('rapport')[1]
    path = path.replace(os.sep, '.').rsplit('.', 1)[0]
    return path