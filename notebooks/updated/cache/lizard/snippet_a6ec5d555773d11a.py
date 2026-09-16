def tile_fonts(self, fontstack, stack_range, out_folder=None):
    url = '{url}/resources/fonts/{fontstack}/{stack_range}.pbf'.format(url=
        self._url, fontstack=fontstack, stack_range=stack_range)
    params = {}
    if out_folder is None:
        out_folder = tempfile.gettempdir()
    return self._get(url=url, param_dict=params, out_folder=out_folder,
        securityHandler=self._securityHandler, proxy_port=self._proxy_port,
        proxy_url=self._proxy_host)