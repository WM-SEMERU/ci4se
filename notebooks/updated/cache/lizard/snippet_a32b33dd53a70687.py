def pack(self, value=None):
    if value is None:
        data_backup = None
        if self.data is not None and not isinstance(self.data, bytes):
            data_backup = self.data
            self.data = self.data.pack()
        packed = super().pack()
        if data_backup is not None:
            self.data = data_backup
        return packed
    elif isinstance(value, type(self)):
        return value.pack()
    else:
        msg = '{} is not an instance of {}'.format(value, type(self).__name__)
        raise PackException(msg)