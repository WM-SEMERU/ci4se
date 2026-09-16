def unpack(self, buff, offset=0):
    super().unpack(buff)
    class_name = self._get_body_class()
    buff = self.body.value
    self.body = FixedTypeList(pyof_class=class_name)
    self.body.unpack(buff)