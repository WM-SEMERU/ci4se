def _is_instance(type_to_check, element, condition='any', deep=False):
    out = None
    if deep is False:
        if condition == 'any':
            out = any(isinstance(el, type_to_check) for el in element)
        elif condition == 'all':
            out = all(isinstance(el, type_to_check) for el in element)
    else:
        for row in range(0, len(element)):
            for column in range(0, len(element[row])):
                flag = _is_instance(type_to_check, element[column][row],
                    'all', deep=False)
                if flag is False:
                    out = flag
                else:
                    out = True
    return out