def read(self, ulBuffer, pDst, unBytes):
    fn = self.function_table.read
    punRead = c_uint32()
    result = fn(ulBuffer, pDst, unBytes, byref(punRead))
    return result, punRead.value