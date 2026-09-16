def trim_decimals(s, precision=-3):
    encoded = s.encode('ascii', 'ignore')
    str_val = ''
    if six.PY3:
        str_val = str(encoded, encoding='ascii', errors='ignore')[:precision]
    elif precision == 0:
        str_val = str(encoded)
    else:
        str_val = str(encoded)[:precision]
    if len(str_val) > 0:
        return float(str_val)
    else:
        return 0