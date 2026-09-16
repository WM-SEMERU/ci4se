def authenticate(self, username, password):
    user = self.get_by_username_or_email(username)
    if not user:
        return None
    if user.check_password(password):
        return user
    return None