def create_access_key(self, name, is_active=True, permitted=[], options={}):
    return self.api.create_access_key(name=name, is_active=is_active,
        permitted=permitted, options=options)