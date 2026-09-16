def sign_direct(self, request, authheaders, secret):
    if request.get_header('x-authorization-timestamp') == '':
        request.with_header('X-Authorization-Timestamp', str(time.time()))
    if request.body is not None and request.body != b'':
        if request.get_header('x-authorization-content-sha256') == '':
            sha256 = hashlib.sha256()
            sha256.update(request.body)
            request.with_header('X-Authorization-Content-SHA256', base64.
                b64encode(sha256.digest()).decode('utf-8'))
    sig = self.sign(request, authheaders, secret)
    authheaders['signature'] = sig
    return request.with_header('Authorization', 'acquia-http-hmac {0}'.
        format(self.unroll_auth_headers(authheaders)))