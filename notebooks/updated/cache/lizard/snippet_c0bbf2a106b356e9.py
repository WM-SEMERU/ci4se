def get_access_key(self):
    access_key = self.get_as_nullable_string('access_key')
    access_key = (access_key if access_key != None else self.
        get_as_nullable_string('access_key'))
    return access_key