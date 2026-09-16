def _create_tree(self, endpoint=None, index=0):
    tab = ''
    ret = ''
    if endpoint:
        name = endpoint.path.split('.', 1)[1].replace('.', '/') + '/'
        ret += tab + name + '\n'
        ret += endpoint.method_calls(' ' * len(tab + name))
    else:
        endpoint = self
    for child_name in endpoint._endpoints:
        child = getattr(endpoint, child_name, None)
        if child:
            ret += self._create_tree(child, index + 1)
    return ret