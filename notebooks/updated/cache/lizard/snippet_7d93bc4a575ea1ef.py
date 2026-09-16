def hexify(number):
    if isinstance(number, int) == False:
        raise TypeError('hexify(): expected integer, not {}'.format(type(
            number)))
    if number < 0:
        raise ValueError('Invalid number to hexify - must be positive')
    result = hex(int(number)).replace('0x', '').upper()
    if divmod(len(result), 2)[1] == 1:
        result = '0{}'.format(result)
    return result