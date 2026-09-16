def ACC_calc(TP, TN, FP, FN):
    try:
        result = (TP + TN) / (TP + TN + FN + FP)
        return result
    except ZeroDivisionError:
        return 'None'