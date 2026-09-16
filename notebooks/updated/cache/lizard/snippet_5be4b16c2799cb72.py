def validateObjectPath(p):
    if not p.startswith('/'):
        raise MarshallingError('Object paths must begin with a "/"')
    if len(p) > 1 and p[-1] == '/':
        raise MarshallingError('Object paths may not end with "/"')
    if '//' in p:
        raise MarshallingError('"//" is not allowed in object paths"')
    if invalid_obj_path_re.search(p):
        raise MarshallingError('Invalid characters contained in object path')