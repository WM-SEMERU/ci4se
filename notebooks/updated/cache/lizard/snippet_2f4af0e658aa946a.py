def ConvCnstrMOD(*args, **kwargs):
    if 'method' in kwargs:
        method = kwargs['method']
        del kwargs['method']
    else:
        method = 'cns'
    if method == 'ism':
        base = ConvCnstrMOD_IterSM
    elif method == 'cg':
        base = ConvCnstrMOD_CG
    elif method == 'cns':
        base = ConvCnstrMOD_Consensus
    else:
        raise ValueError('Unknown ConvCnstrMOD solver method %s' % method)


    class ConvCnstrMOD(base):

        def __init__(self, *args, **kwargs):
            super(ConvCnstrMOD, self).__init__(*args, **kwargs)
    _fix_dynamic_class_lookup(ConvCnstrMOD, method)
    return ConvCnstrMOD(*args, **kwargs)