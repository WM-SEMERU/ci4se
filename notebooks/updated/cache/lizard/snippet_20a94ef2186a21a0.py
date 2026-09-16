def get_output_every(dirname):
    fnames = get_filenames(dirname)
    i_s = np.array([_f_to_i(fname) for fname in fnames])
    everys = list(set(np.diff(i_s)))
    if len(everys) > 1:
        raise TypeError('Multiple values for `output_every` found, {}.'.
            format(everys))
    return everys[0]