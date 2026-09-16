def verify_request(self, query, binding):
    resp_args = {}
    if not query:
        logger.info('Missing QUERY')
        resp = Unauthorized('Unknown user')
        return resp_args, resp(self.environ, self.start_response)
    if not self.req_info:
        self.req_info = IDP.parse_authn_request(query, binding)
    logger.info('parsed OK')
    _authn_req = self.req_info.message
    logger.debug('%s', _authn_req)
    try:
        self.binding_out, self.destination = IDP.pick_binding(
            'assertion_consumer_service', bindings=self.response_bindings,
            entity_id=_authn_req.issuer.text, request=_authn_req)
    except Exception as err:
        logger.error("Couldn't find receiver endpoint: %s", err)
        raise
    logger.debug('Binding: %s, destination: %s', self.binding_out, self.
        destination)
    resp_args = {}
    try:
        resp_args = IDP.response_args(_authn_req)
        _resp = None
    except UnknownPrincipal as excp:
        _resp = IDP.create_error_response(_authn_req.id, self.destination, excp
            )
    except UnsupportedBinding as excp:
        _resp = IDP.create_error_response(_authn_req.id, self.destination, excp
            )
    return resp_args, _resp