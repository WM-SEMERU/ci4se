def update(self, command=None, **kwargs):
    if command is None:
        argparser = self.argparser
    else:
        argparser = self[command]
    for k, v in kwargs.items():
        setattr(argparser, k, v)