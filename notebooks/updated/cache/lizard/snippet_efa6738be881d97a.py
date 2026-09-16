def confusion_to_mcc(*args):
    if len(args) is 1:
        tn, fp, fn, tp = args[0].ravel().astype(float)
    elif len(args) is 4:
        tn, fp, fn, tp = [float(a) for a in args]
    else:
        raise Exception(
            'Input argument is not an 2x2 matrix, nor 4 elements tn, fp, fn, tp.'
            )
    return (tp * tn - fp * fn) / np.sqrt((tp + fp) * (tp + fn) * (tn + fp) *
        (tn + fn))