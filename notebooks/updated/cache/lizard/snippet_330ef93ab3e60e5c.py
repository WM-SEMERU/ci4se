def calc_offset(lines, target, invert_search=False):
    if target and target[0] is not None:
        for offset, line in enumerate(l.strip() for l in lines):
            found_any = any([line.startswith(t) for t in target])
            if not invert_search and found_any:
                return offset
            elif invert_search and not (line == '' or found_any):
                return offset
        raise ValueError("Line containing '{}' was not found in table".
            format(','.join(target)))
    else:
        return 0