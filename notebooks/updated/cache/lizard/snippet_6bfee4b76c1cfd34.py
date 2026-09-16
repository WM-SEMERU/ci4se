def object_hook(dct):
    try:
        if 'BOOL' in dct:
            return dct['BOOL']
        if 'S' in dct:
            val = dct['S']
            try:
                return datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f')
            except:
                return str(val)
        if 'SS' in dct:
            return list(dct['SS'])
        if 'N' in dct:
            if re.match('^-?\\d+?\\.\\d+?$', dct['N']) is not None:
                return float(dct['N'])
            else:
                try:
                    return int(dct['N'])
                except:
                    return int(dct['N'])
        if 'B' in dct:
            return str(dct['B'])
        if 'NS' in dct:
            return set(dct['NS'])
        if 'BS' in dct:
            return set(dct['BS'])
        if 'M' in dct:
            return dct['M']
        if 'L' in dct:
            return dct['L']
        if 'NULL' in dct and dct['NULL'] is True:
            return None
    except:
        return dct
    for key, val in six.iteritems(dct):
        if isinstance(val, six.string_types):
            try:
                dct[key] = datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f')
            except:
                pass
        if isinstance(val, Decimal):
            if val % 1 > 0:
                dct[key] = float(val)
            elif six.PY3:
                dct[key] = int(val)
            elif val < sys.maxsize:
                dct[key] = int(val)
            else:
                dct[key] = long(val)
    return dct