def filedet(name, fobj=None, suffix=None):
    name = name or fobj and fobj.name or suffix
    separated = name.split('.')
    if len(separated) == 1:
        raise FiledetException('file name error.')
    key = '.' + separated[-1]
    return _file_type_map.get(key)