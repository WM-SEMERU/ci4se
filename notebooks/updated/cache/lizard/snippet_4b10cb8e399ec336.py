def convertDict2Attrs(self, *args, **kwargs):
    for n, l in enumerate(self.attrs):
        try:
            params = self.params
        except AttributeError as aerr:
            params = {}
        kwargs.update(params)
        try:
            loan = self.mambuloanclass(*args, urlfunc=None, entid=None, **
                kwargs)
        except AttributeError as ae:
            self.mambuloanclass = self.itemclass
            loan = self.mambuloanclass(*args, urlfunc=None, entid=None, **
                kwargs)
        loan.init(l, *args, **kwargs)
        self.attrs[n] = loan