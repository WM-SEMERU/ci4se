def rcts(self, command, *args, **kwargs):
    cls = self.__class__
    name = kwargs.pop('name', '')
    date = kwargs.pop('date', None)
    data = kwargs.pop('data', None)
    kwargs.pop('bycolumn', None)
    ts = cls(name=name, date=date, data=data)
    ts._ts = self.rc(command, *args, **kwargs)
    return ts