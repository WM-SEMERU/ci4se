def _av_weight(W1, W2):
    if str(W1) in [' ', '']:
        W1 = 1
    elif str(W1) in ['-9', '9', '9.0', '-9.0']:
        W1 = 0
    elif float(W1) < 0:
        warnings.warn('Negative weight found, setting to zero')
        W1 = 0
    else:
        W1 = 1 - int(W1) / 4.0
    if str(W2) in [' ', '']:
        W2 = 1
    elif str(W2) in ['-9', '9', '9.0', '-9.0']:
        W2 = 0
    elif float(W2) < 0:
        warnings.warn('Negative weight found, setting to zero')
        W2 = 0
    else:
        W2 = 1 - int(W2) / 4.0
    W = (W1 + W2) / 2
    if W < 0:
        print('Weight 1: ' + str(W1))
        print('Weight 2: ' + str(W2))
        print('Final weight: ' + str(W))
        raise IOError('Negative average weight calculated, setting to zero')
    return _cc_round(W, 4)