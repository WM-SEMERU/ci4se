def vat_id(self):

    def _checksum(digits):
        code = ['8', '6', '4', '2', '3', '5', '9', '7']
        remainder = 11 - sum(map(lambda x, y: int(x) * int(y), code, digits)
            ) % 11
        if remainder == 10:
            return 0
        elif remainder == 11:
            return 5
        return remainder
    vat_id = self.bothify('########')
    return 'CHE' + vat_id + str(_checksum(vat_id))