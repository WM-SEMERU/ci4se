def getStatus(self):
    status = self.single_read(self.AD7730_STATUS_REG)
    bits_values = dict([('NOREF', status[0] & 16 == 16), ('STBY', status[0] &
        32 == 32), ('STDY', status[0] & 64 == 64), ('RDY', status[0] & 128 ==
        128)])
    return bits_values