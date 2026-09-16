def decimal_precision(row):
    try:
        row = list(row)
        for idx, x in enumerate(row):
            x = str(x)
            m = re.match(re_sci_notation, x)
            if m:
                _x2 = round(float(m.group(2)), 3)
                x = m.group(1) + str(_x2)[1:] + m.group(3)
            else:
                try:
                    x = round(float(x), 3)
                except (ValueError, TypeError):
                    x = x
            row[idx] = x
        row = tuple(row)
    except Exception as e:
        print(
            'Error: Unable to fix the precision of values. File size may be larger than normal, {}'
            .format(e))
    return row