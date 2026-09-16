def _createdby_data(self, ws):
    username = ws.getOwner().getUserName()
    return {'username': username, 'fullname': to_utf8(self.user_fullname(
        username)), 'email': to_utf8(self.user_email(username))}