def decimal_str_to_int(decimal_string):
    int_string = decimal_string.replace('.', '')
    int_string = int_string.lstrip('0')
    return int(int_string)