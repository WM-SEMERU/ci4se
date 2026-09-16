def _validate_signature(self, request, principal, args, params):
    creds = AWSCredentials(principal.access_key, principal.secret_key)
    endpoint = AWSServiceEndpoint()
    endpoint.set_method(request.method)
    endpoint.set_canonical_host(request.getHeader('Host'))
    path = request.path
    if self.path is not None:
        path = '%s/%s' % (self.path.rstrip('/'), path.lstrip('/'))
    endpoint.set_path(path)
    signature = Signature(creds, endpoint, params, signature_method=args[
        'signature_method'], signature_version=args['signature_version'])
    if signature.compute() != args['signature']:
        raise APIError(403, 'SignatureDoesNotMatch',
            'The request signature we calculated does not match the signature you provided. Check your key and signing method.'
            )