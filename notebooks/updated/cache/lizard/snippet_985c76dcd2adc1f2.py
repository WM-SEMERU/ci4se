def get_auth_token(cls):
    if 'Authorization' not in f_request.headers:
        raise ValueError('Missing Authorization Bearer in headers')
    data = f_request.headers['Authorization'].encode('ascii', 'ignore')
    return str.replace(str(data), 'Bearer ', '').strip()