def select_matchedfilter_class(curr_exe):
    exe_to_class_map = {'pycbc_inspiral': PyCBCInspiralExecutable,
        'pycbc_inspiral_skymax': PyCBCInspiralExecutable,
        'pycbc_multi_inspiral': PyCBCMultiInspiralExecutable}
    try:
        return exe_to_class_map[curr_exe]
    except KeyError:
        raise NotImplementedError(
            'No job class exists for executable %s, exiting' % curr_exe)