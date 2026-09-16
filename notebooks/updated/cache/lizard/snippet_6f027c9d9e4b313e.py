def pack(self, value=None):
    buff = self.body
    if not value:
        value = self.body
    if value:
        if isinstance(value, (list, FixedTypeList)):
            obj = self._get_body_instance()
            obj.extend(value)
        elif hasattr(value, 'pack'):
            obj = value
        self.body = obj.pack()
    multipart_packed = super().pack()
    self.body = buff
    return multipart_packed