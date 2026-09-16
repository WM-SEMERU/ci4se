def label_both(label_info, multi_line=True, sep=': '):
    label_info = label_info.astype(str)
    for var in label_info.index:
        label_info[var] = '{0}{1}{2}'.format(var, sep, label_info[var])
    if not multi_line:
        label_info = collapse_label_lines(label_info)
    return label_info