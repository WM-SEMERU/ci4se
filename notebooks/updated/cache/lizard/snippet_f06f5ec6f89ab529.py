def get_var(self, name, user=None):
    if user is not None:
        if user not in self._users:
            raise UserNotDefinedError
        return self._users[user].get_var(name)
    if name not in self._global_vars:
        raise VarNotDefinedError
    return self._global_vars[name]