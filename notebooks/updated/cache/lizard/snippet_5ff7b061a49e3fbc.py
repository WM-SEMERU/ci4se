def insert(self, context):
    module_file = open(context.resolve(self.__path), 'rb')
    data = {'name': self.__name}
    if self.__context_root is not None:
        data['contextroot'] = self.__context_root
    status_code, msg = self.__endpoint.post('/applications/application',
        data=data, files={'id': module_file}, timeout=60.0)
    module_file.close()
    self.__available = True