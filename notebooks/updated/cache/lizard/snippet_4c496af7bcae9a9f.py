def _get_op_name(op, special):
    opname = op.__name__.strip('_')
    if special:
        opname = '__{opname}__'.format(opname=opname)
    return opname