def create_ecp_authn_request(self, entityid=None, relay_state='', sign=
    False, **kwargs):
    my_url = self.service_urls(BINDING_PAOS)[0]
    paos_request = paos.Request(must_understand='1', actor=ACTOR,
        response_consumer_url=my_url, service=ECP_SERVICE)
    relay_state = ecp.RelayState(actor=ACTOR, must_understand='1', text=
        relay_state)
    try:
        authn_req = kwargs['authn_req']
        try:
            req_id = authn_req.id
        except AttributeError:
            req_id = 0
    except KeyError:
        try:
            _binding = kwargs['binding']
        except KeyError:
            _binding = BINDING_SOAP
            kwargs['binding'] = _binding
        logger.debug('entityid: %s, binding: %s', entityid, _binding)
        _, location = self.pick_binding('single_sign_on_service', [_binding
            ], entity_id=entityid)
        req_id, authn_req = self.create_authn_request(location,
            service_url_binding=BINDING_PAOS, **kwargs)
    soap_envelope = make_soap_enveloped_saml_thingy(authn_req, [
        paos_request, relay_state])
    return req_id, '%s' % soap_envelope