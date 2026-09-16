def cleanup(first_I, first_Z):
    cont = 0
    Nmin = len(first_I)
    if len(first_Z) < Nmin:
        Nmin = len(first_Z)
    for kk in range(Nmin):
        if first_I[kk][0] != first_Z[kk][0]:
            print('\n WARNING: ')
            if first_I[kk] < first_Z[kk]:
                del first_I[kk]
            else:
                del first_Z[kk]
            print('Unmatched step number: ', kk + 1, '  ignored')
            cont = 1
        if cont == 1:
            return first_I, first_Z, cont
    return first_I, first_Z, cont