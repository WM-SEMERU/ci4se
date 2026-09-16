def add_props(self, **kwargs):
    for kw, val in kwargs.iteritems():
        self.properties[kw] = val