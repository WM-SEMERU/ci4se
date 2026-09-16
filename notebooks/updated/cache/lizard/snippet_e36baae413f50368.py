def get_password(self):
    if self.password is None:
        if os.environ.get(self.username + 'password'):
            self.password = os.environ.get(self.username + 'password')
        else:
            raise PasswordError(self.username)