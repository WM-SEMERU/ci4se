def encode_basic_auth(username, password):
    return 'Basic {}'.format(b64encode('{}:{}'.format(username, password).
        encode('utf-8')).decode('utf-8'))