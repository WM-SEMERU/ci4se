def response_type_is_in_registered_response_types(provider,
    authentication_request):
    error = InvalidAuthenticationRequest('Response type is not registered',
        authentication_request, oauth_error='invalid_request')
    try:
        allowed_response_types = provider.clients[authentication_request[
            'client_id']]['response_types']
    except KeyError as e:
        logger.error('client metadata is missing response_types')
        raise error
    if not is_allowed_response_type(authentication_request['response_type'],
        allowed_response_types):
        logger.error("Response type '{}' is not registered".format(' '.join
            (authentication_request['response_type'])))
        raise error