def get_object(self, cat, **kwargs):
    if 'id' not in kwargs.keys():
        kwargs['id'] = ''
    res = request.get_object_cat1(self.con, self.token, cat, kwargs)
    return res