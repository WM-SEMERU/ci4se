def unpack_from(self, buff, offset=0):
    return self._create(super(DictStruct, self).unpack_from(buff, offset))