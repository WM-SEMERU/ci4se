def fetch_all_kernels(self):
    r
    api = self.doapi_manager
    for kern in api.paginate(self.url + '/kernels', 'kernels'):
        yield Kernel(kern, doapi_manager=api)