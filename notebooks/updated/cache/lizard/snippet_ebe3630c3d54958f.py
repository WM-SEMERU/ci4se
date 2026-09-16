def checksum(digits, scale):
    chk_nbr = 11 - sum(map(operator.mul, digits, scale)) % 11
    if chk_nbr == 11:
        return 0
    return chk_nbr