def request_pdu(self):
    if None in [self.address, self.value]:
        raise Exception
    return struct.pack('>BH' + conf.TYPE_CHAR, self.function_code, self.
        address, self.value)