def _get_rest_doc(self, request, start_response):
    api = request.body_json['api']
    version = request.body_json['version']
    generator = discovery_generator.DiscoveryGenerator(request=request)
    services = [s for s in self._backend.api_services if s.api_info.name ==
        api and s.api_info.api_version == version]
    doc = generator.pretty_print_config_to_json(services)
    if not doc:
        error_msg = (
            'Failed to convert .api to discovery doc for version %s of api %s'
             % (version, api))
        _logger.error('%s', error_msg)
        return util.send_wsgi_error_response(error_msg, start_response)
    return self._send_success_response(doc, start_response)