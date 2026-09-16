def prepare_for_negotiated_authenticate(self, entityid=None, relay_state='',
    binding=None, vorg='', nameid_format=None, scoping=None, consent=None,
    extensions=None, sign=None, response_binding=saml2.BINDING_HTTP_POST,
    **kwargs):
    expected_binding = binding
    for binding in [BINDING_HTTP_REDIRECT, BINDING_HTTP_POST]:
        if expected_binding and binding != expected_binding:
            continue
        destination = self._sso_location(entityid, binding)
        logger.info('destination to provider: %s', destination)
        reqid, request = self.create_authn_request(destination, vorg,
            scoping, response_binding, nameid_format, consent=consent,
            extensions=extensions, sign=sign, **kwargs)
        _req_str = str(request)
        logger.info('AuthNReq: %s', _req_str)
        try:
            args = {'sigalg': kwargs['sigalg']}
        except KeyError:
            args = {}
        http_info = self.apply_binding(binding, _req_str, destination,
            relay_state, sign=sign, **args)
        return reqid, binding, http_info
    else:
        raise SignOnError('No supported bindings available for authentication')