def client_id_is_known(provider, authentication_request):
    if authentication_request['client_id'] not in provider.clients:
        logger.error("Unknown client_id '{}'".format(authentication_request
            ['client_id']))
        raise InvalidAuthenticationRequest('Unknown client_id',
            authentication_request, oauth_error='unauthorized_client')