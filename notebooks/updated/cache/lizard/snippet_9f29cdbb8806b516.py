def val_to_mrc(code, val):
    code = str(code)
    if len(code) < 3:
        code += (3 - len(code)) * ' '
    return '%s   L %s' % (code, val)