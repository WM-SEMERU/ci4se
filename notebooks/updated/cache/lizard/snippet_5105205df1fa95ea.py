def update(self, dictionary=None, **kwargs):
    if not dictionary == None:
        kwargs.update(dictionary)
    for k in list(kwargs.keys()):
        self[k] = kwargs[k]