def dotopdict(self, dict_):
    mlookup = {'get': 'GET', 'post': 'POST'}

    def rearrange(path, method_dict, method):
        oid = method_dict['operationId']
        self._paths[oid] = path
        method_dict['nickname'] = oid
        method_dict['method'] = mlookup[method]
    paths = dict_['paths']
    for path, path_dict in paths.items():
        if self.path_prefix and self.path_prefix not in path:
            continue
        path_dict['operations'] = []
        for method, method_dict in sorted(path_dict.items()):
            if method == 'operations':
                continue
            rearrange(path, method_dict, method)
            path_dict['operations'].append(method_dict)
        path_dict['path'] = path

    def setp(v, lenp=len(self.path_prefix)):
        v['path'] = v['path'][lenp:]
        return v
    dict_['apis'] = []
    for tag_dict in dict_['tags']:
        path = '/' + tag_dict['name']
        d = {'path': path, 'description': tag_dict['description'],
            'class_json': {'docstring': tag_dict['description'],
            'resourcePath': path, 'apis': [setp(v) for k, v in paths.items(
            ) if k.startswith(self.path_prefix + path)]}}
        dict_['apis'].append(d)
    self._swagger(dict_['swagger'])
    self._info(dict_['info'])
    self._definitions(dict_['definitions'])
    return dict_