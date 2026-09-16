def authn_response(self, context, binding):
    if not context.request['SAMLResponse']:
        satosa_logging(logger, logging.DEBUG, 'Missing Response for state',
            context.state)
        raise SATOSAAuthenticationError(context.state, 'Missing Response')
    try:
        authn_response = self.sp.parse_authn_request_response(context.
            request['SAMLResponse'], binding, outstanding=self.
            outstanding_queries)
    except Exception as err:
        satosa_logging(logger, logging.DEBUG,
            'Failed to parse authn request for state', context.state,
            exc_info=True)
        raise SATOSAAuthenticationError(context.state,
            'Failed to parse authn request') from err
    if self.sp.config.getattr('allow_unsolicited', 'sp') is False:
        req_id = authn_response.in_response_to
        if req_id not in self.outstanding_queries:
            errmsg = 'No request with id: {}'.format(req_id),
            satosa_logging(logger, logging.DEBUG, errmsg, context.state)
            raise SATOSAAuthenticationError(context.state, errmsg)
        del self.outstanding_queries[req_id]
    if context.state[self.name]['relay_state'] != context.request['RelayState'
        ]:
        satosa_logging(logger, logging.DEBUG,
            'State did not match relay state for state', context.state)
        raise SATOSAAuthenticationError(context.state,
            'State did not match relay state')
    context.decorate(Context.KEY_BACKEND_METADATA_STORE, self.sp.metadata)
    del context.state[self.name]
    return self.auth_callback_func(context, self._translate_response(
        authn_response, context.state))