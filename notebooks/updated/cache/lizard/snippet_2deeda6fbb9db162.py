def get_users(self, search=None, page=1, per_page=20, **kwargs):
    if search:
        return self.get('/users', page=page, per_page=per_page, search=
            search, **kwargs)
    return self.get('/users', page=page, per_page=per_page, **kwargs)