def select_tmpltbank_class(curr_exe):
    exe_to_class_map = {'pycbc_geom_nonspinbank': PyCBCTmpltbankExecutable,
        'pycbc_aligned_stoch_bank': PyCBCTmpltbankExecutable}
    try:
        return exe_to_class_map[curr_exe]
    except KeyError:
        raise NotImplementedError(
            'No job class exists for executable %s, exiting' % curr_exe)