def _parse_typedef(line, _rawtypedef):
    if '[Typedef]' in line:
        _rawtypedef.append(collections.defaultdict(list))
    else:
        key, value = line.split(':', 1)
        _rawtypedef[-1][key.strip()].append(value.strip())