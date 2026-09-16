def printableVal(val, type_bit=True, justlength=False):
    from utool import util_dev
    import numpy as np
    if type(val) is np.ndarray:
        info = npArrInfo(val)
        if info.dtypestr.startswith('bool'):
            _valstr = ('{ shape:' + info.shapestr + ' bittotal: ' + info.
                bittotal + '}')
        elif info.dtypestr.startswith('float'):
            _valstr = util_dev.get_stats_str(val)
        else:
            _valstr = ('{ shape:' + info.shapestr + ' mM:' + info.minmaxstr +
                ' }')
    elif isinstance(val, (str, unicode)):
        _valstr = "'%s'" % val
    elif isinstance(val, list):
        if justlength or len(val) > 30:
            _valstr = 'len=' + str(len(val))
        else:
            _valstr = '[ ' + ', \n  '.join([str(v) for v in val]) + ' ]'
    elif hasattr(val, 'get_printable') and type(val) != type:
        _valstr = val.get_printable(type_bit=type_bit)
    elif isinstance(val, dict):
        _valstr = '{\n'
        for val_key in val.keys():
            val_val = val[val_key]
            _valstr += '  ' + str(val_key) + ' : ' + str(val_val) + '\n'
        _valstr += '}'
    else:
        _valstr = str(val)
    if _valstr.find('\n') > 0:
        _valstr = _valstr.replace('\n', '\n    ')
        _valstr = '\n    ' + _valstr
    _valstr = re.sub('\n *$', '', _valstr)
    return _valstr