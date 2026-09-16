def _jgezerou16(ins):
    output = []
    value = ins.quad[1]
    if not is_int(value):
        output = _16bit_oper(value)
    output.append('jp %s' % str(ins.quad[2]))
    return output