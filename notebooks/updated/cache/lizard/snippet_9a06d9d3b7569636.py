def _int_size(x):
    if -128 <= x <= 127:
        return 1
    elif -32768 <= x <= 32767:
        return 2
    elif -2147483648 <= x <= 2147483647:
        return 4
    elif long(-9223372036854775808) <= x <= long(9223372036854775807):
        return 8
    else:
        raise RuntimeError('Cannot represent value: ' + str(x))