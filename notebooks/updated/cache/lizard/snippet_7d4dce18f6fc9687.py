def register(self, auth_body=None, kind='user', bind_email=None, username=
    None, password=None, device_id=None, initial_device_display_name=None,
    inhibit_login=None):
    content = {}
    content['kind'] = kind
    if auth_body:
        content['auth'] = auth_body
    if username:
        content['username'] = username
    if password:
        content['password'] = password
    if device_id:
        content['device_id'] = device_id
    if initial_device_display_name:
        content['initial_device_display_name'] = initial_device_display_name
    if bind_email:
        content['bind_email'] = bind_email
    if inhibit_login:
        content['inhibit_login'] = inhibit_login
    return self._send('POST', '/register', content=content, query_params={
        'kind': kind})