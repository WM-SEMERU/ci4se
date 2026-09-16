def put(self, username, email=None, full_name=None, password=None, status=
    None, auth_level=None, user_id=None):
    return self.connection.put('user/admin', data=dict(username=username,
        email=email, full_name=full_name, password=password, status=status,
        auth_level=auth_level, user_id=user_id))