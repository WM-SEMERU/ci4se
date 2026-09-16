def compare_dicts(i):
    d1 = i.get('dict1', {})
    d2 = i.get('dict2', {})
    equal = 'yes'
    bic = False
    ic = i.get('ignore_case', '')
    if ic == 'yes':
        bic = True
    for q2 in d2:
        v2 = d2[q2]
        if type(v2) == dict:
            if q2 not in d1:
                equal = 'no'
                break
            v1 = d1[q2]
            rx = compare_dicts({'dict1': v1, 'dict2': v2, 'ignore_case': ic})
            if rx['return'] > 0:
                return rx
            equal = rx['equal']
            if equal == 'no':
                break
        elif type(v2) == list:
            if q2 not in d1:
                equal = 'no'
                break
            v1 = d1[q2]
            if type(v1) != list:
                equal = 'no'
                break
            for m in v2:
                if m not in v1:
                    equal = 'no'
                    break
            if equal == 'no':
                break
        else:
            if q2 not in d1:
                equal = 'no'
                break
            if equal == 'no':
                break
            v1 = d1[q2]
            if bic and type(v1) != int and type(v1) != float and type(v1
                ) != bool:
                v1 = v1.lower()
                v2 = v2.lower()
            if v2 != v1:
                equal = 'no'
                break
    return {'return': 0, 'equal': equal}