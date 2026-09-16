def wc_lha2dict(lha):
    C = OrderedDict()
    for k, (block, i) in WC_dict_0f.items():
        try:
            C[k] = dict(lha['BLOCK'][block]['values'])[i]
        except KeyError:
            C[k] = 0
    for k in definitions.WC_keys_2f:
        try:
            C[k] = lha2matrix(lha['BLOCK']['WC' + k.upper()]['values'], (3, 3)
                ).real
        except KeyError:
            C[k] = np.zeros((3, 3))
        try:
            C[k] = C[k] + 1.0j * lha2matrix(lha['BLOCK']['IMWC' + k.upper()
                ]['values'], (3, 3))
        except KeyError:
            pass
    for k in definitions.WC_keys_4f:
        try:
            C[k] = lha2matrix(lha['BLOCK']['WC' + k.upper()]['values'], (3,
                3, 3, 3))
        except KeyError:
            C[k] = np.zeros((3, 3, 3, 3))
        try:
            C[k] = C[k] + 1.0j * lha2matrix(lha['BLOCK']['IMWC' + k.upper()
                ]['values'], (3, 3, 3, 3))
        except KeyError:
            pass
    return C