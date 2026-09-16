def start_auth(self, context, internal_request, get_state=stateID):
    request_args = dict(client_id=self.config['client_config']['client_id'],
        redirect_uri=self.redirect_url, scope=' '.join(self.config['scope']))
    cis = self.consumer.construct_AuthorizationRequest(request_args=
        request_args)
    return Redirect(cis.request(self.consumer.authorization_endpoint))