def resolve(self, authorization: http.Header):
    if authorization is None:
        return None
    scheme, token = authorization.split()
    if scheme.lower() != 'basic':
        return None
    username, password = base64.b64decode(token).decode('utf-8').split(':')
    user = authenticate(username=username, password=password)
    return user