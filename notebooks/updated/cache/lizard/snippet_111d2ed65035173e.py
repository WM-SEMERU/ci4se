def binary_value(self):
    str_raw_value = str(self.raw_value)
    if len(str_raw_value) % 2 == 1:
        str_raw_value = '0' + str_raw_value
    return binascii.unhexlify(str_raw_value)