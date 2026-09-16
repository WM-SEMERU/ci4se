def __set_checksum(self):
    checksum = self.__get_checksum(self.__out_buffer.raw)
    self.STRUCT_CHECKSUM.pack_into(self.__out_buffer, self.OFFSET_CHECKSUM,
        checksum)