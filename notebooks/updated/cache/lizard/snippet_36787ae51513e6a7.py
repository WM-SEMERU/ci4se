def get_client_kwargs(self, path):
    path = path.split('?', 1)[0]
    share_name, relpath = self.split_locator(path)
    kwargs = dict(share_name=share_name)
    if relpath and relpath[-1] == '/':
        kwargs['directory_name'] = relpath.rstrip('/')
    elif relpath:
        try:
            kwargs['directory_name'], kwargs['file_name'] = relpath.rsplit('/',
                1)
        except ValueError:
            kwargs['directory_name'] = ''
            kwargs['file_name'] = relpath
    return kwargs