def register_name(self, username):
    if self.is_username_used(username):
        raise UsernameInUseException('Username {username} already in use!'.
            format(username=username))
    self.registered_names.append(username)