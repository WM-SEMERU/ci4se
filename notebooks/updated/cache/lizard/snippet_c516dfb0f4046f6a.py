def find(self, path, all=False):
    try:
        start, _, extn = path.rsplit('.', 2)
    except ValueError:
        return []
    path = '.'.join((start, extn))
    return find(path, all=all) or []