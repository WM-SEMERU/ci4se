def _check_str_value(x):
    if isinstance(x, str):
        x = x.replace(',', '.').replace(chr(8216), "'").replace(chr(8217), "'")
        if ' ' in x:
            if x[0] in ('"', "'"):
                x = x[1:]
            if x[-1] in ('"', "'"):
                x = x[:len(x) - 1]
            x = '"' + x.replace('"', '\\"') + '"'
    return str(x)