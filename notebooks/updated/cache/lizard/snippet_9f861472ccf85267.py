def time_label(intvl, return_val=True):
    if type(intvl) in [list, tuple, np.ndarray] and len(intvl) == 1:
        label = '{:02}'.format(intvl[0])
        value = np.array(intvl)
    elif type(intvl) == int and intvl in range(1, 13):
        label = '{:02}'.format(intvl)
        value = np.array([intvl])
    else:
        labels = {'jfm': (1, 2, 3), 'fma': (2, 3, 4), 'mam': (3, 4, 5),
            'amj': (4, 5, 6), 'mjj': (5, 6, 7), 'jja': (6, 7, 8), 'jas': (7,
            8, 9), 'aso': (8, 9, 10), 'son': (9, 10, 11), 'ond': (10, 11, 
            12), 'ndj': (11, 12, 1), 'djf': (1, 2, 12), 'jjas': (6, 7, 8, 9
            ), 'djfm': (12, 1, 2, 3), 'ann': range(1, 13)}
        for lbl, vals in labels.items():
            if intvl == lbl or set(intvl) == set(vals):
                label = lbl
                value = np.array(vals)
                break
    if return_val:
        return label, value
    else:
        return label