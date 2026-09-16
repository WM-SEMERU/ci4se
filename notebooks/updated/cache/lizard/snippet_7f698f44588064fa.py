def start(self):
    routing_list = self._make_routing_list(self.api_provider)
    if not routing_list:
        raise NoApisDefined('No APIs available in SAM template')
    static_dir_path = self._make_static_dir_path(self.cwd, self.static_dir)
    service = LocalApigwService(routing_list=routing_list, lambda_runner=
        self.lambda_runner, static_dir=static_dir_path, port=self.port,
        host=self.host, stderr=self.stderr_stream)
    service.create()
    self._print_routes(self.api_provider, self.host, self.port)
    LOG.info(
        'You can now browse to the above endpoints to invoke your functions. You do not need to restart/reload SAM CLI while working on your functions, changes will be reflected instantly/automatically. You only need to restart SAM CLI if you update your AWS SAM template'
        )
    service.run()