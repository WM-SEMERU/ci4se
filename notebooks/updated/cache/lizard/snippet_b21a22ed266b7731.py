def validate_authorization_request(self, request):
    if request.prompt == 'none':
        raise OIDCNoPrompt()
    else:
        return self.proxy_target.validate_authorization_request(request)