def get_signum(val, err, max_sig=numpy.inf):
    coeff, pwr = ('%e' % err).split('e')
    if pwr.startswith('-'):
        pwr = int(pwr[1:])
        if round(float(coeff)) == 10.0:
            pwr -= 1
        pwr = min(pwr, max_sig)
        tmplt = '%.' + str(pwr + 1) + 'f'
        return tmplt % val
    else:
        pwr = int(pwr[1:])
        if round(float(coeff)) == 10.0:
            pwr += 1
        return_val = round(val, -pwr + 1)
        if val != 0.0:
            loop_count = 0
            max_recursion = 100
            while return_val == 0.0:
                pwr -= 1
                return_val = round(val, -pwr + 1)
                loop_count += 1
                if loop_count > max_recursion:
                    raise ValueError('Maximum recursion depth hit! Input ' +
                        'values are: val = %f, err = %f' % (val, err))
        return drop_trailing_zeros(return_val)