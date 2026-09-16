def _find_error(vals):
    err_vals = []
    for en in vals:
        c = en[2]
        conc = [(float(i) / sum(c)) for i in c]
        err = abs(en[0] - en[1])
        err_vals.append([conc, err])
    return err_vals