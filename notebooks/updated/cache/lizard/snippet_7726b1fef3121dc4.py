def _trim_zeros_complex(str_complexes, na_rep='NaN'):

    def separate_and_trim(str_complex, na_rep):
        num_arr = str_complex.split('+')
        return _trim_zeros_float([num_arr[0]], na_rep) + ['+'
            ] + _trim_zeros_float([num_arr[1][:-1]], na_rep) + ['j']
    return [''.join(separate_and_trim(x, na_rep)) for x in str_complexes]