def authenticate(self, username=None, password=None):
    data = api_client.authenticate(username, password)
    if not data:
        return
    return User(data.get('pk'), data.get('token'), data.get('user_data'))