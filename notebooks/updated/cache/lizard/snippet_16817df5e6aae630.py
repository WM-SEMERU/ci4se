def convertDict2Attrs(self, *args, **kwargs):
    for n, u in enumerate(self.attrs):
        try:
            params = self.params
        except AttributeError as aerr:
            params = {}
        kwargs.update(params)
        try:
            user = self.mambuuserclass(*args, urlfunc=None, entid=None, **
                kwargs)
        except AttributeError as ae:
            self.mambuuserclass = self.itemclass
            user = self.mambuuserclass(*args, urlfunc=None, entid=None, **
                kwargs)
        user.init(u, *args, **kwargs)
        self.attrs[n] = user