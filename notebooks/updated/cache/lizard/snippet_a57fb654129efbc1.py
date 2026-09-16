def find_declare_doc(self, d, name):
    path = None
    while True:
        if exists(name):
            path = name
            break
        try:
            path = declaration_path(name)
            break
        except IncludeError:
            pass
        for fn in (join(d, name), join(d, name + '.csv')):
            if exists(fn):
                path = fn
                break
        if path:
            break
        if name.startswith('http'):
            path = name.strip('/')
            break
        elif exists(name):
            path = name
            break
        else:
            path = self.resolver.find_decl_doc(name)
            break
        raise IncludeError("No local declaration file for '{}'".format(name))
    return parse_app_url(path)