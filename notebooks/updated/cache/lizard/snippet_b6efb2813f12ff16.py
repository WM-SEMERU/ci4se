def classify_file(f):
    cols = f[1].columns
    if len(cols) == 2:
        return True, False
    elif len(cols) == 3 and 'ERROR' in cols.names:
        return True, True
    elif len(cols) > 2 and 'ERROR' not in cols.names:
        return True, False
    else:
        return False, True