def _index_idiom(el_name, index, alt=None):
    el_index = '%s[%d]' % (el_name, index)
    if index == 0:
        cond = '%s' % el_name
    else:
        cond = 'len(%s) - 1 >= %d' % (el_name, index)
    output = IND + '# pick element from list\n'
    return output + IND + '%s = %s if %s else %s\n\n' % (el_name, el_index,
        cond, repr(alt))