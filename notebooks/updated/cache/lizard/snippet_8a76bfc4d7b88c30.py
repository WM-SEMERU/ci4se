def phone():
    result = ''
    result += '(' + str(RandomInteger.next_integer(111, 999)) + ') '
    result += str(RandomInteger.next_integer(111, 999))
    result += '-' + str(RandomInteger.next_integer(0, 9999))
    return result