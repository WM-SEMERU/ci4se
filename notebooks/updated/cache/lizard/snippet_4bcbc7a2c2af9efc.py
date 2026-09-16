def pretty_print_list(lst, name='features', repr_format=True):
    if not lst or len(lst) < 8:
        if repr_format:
            return lst.__repr__()
        else:
            return ', '.join(map(str, lst))
    else:
        topk = ', '.join(map(str, lst[:3]))
        if repr_format:
            lst_separator = '['
            lst_end_separator = ']'
        else:
            lst_separator = ''
            lst_end_separator = ''
        return '{start}{topk}, ... {last}{end} (total {size} {name})'.format(
            topk=topk, last=lst[-1], name=name, size=len(lst), start=
            lst_separator, end=lst_end_separator)