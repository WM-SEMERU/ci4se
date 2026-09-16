def _leu8(ins):
    output = _8bit_oper(ins.quad[2], ins.quad[3], reversed_=True)
    output.append('sub h')
    output.append('ccf')
    output.append('sbc a, a')
    output.append('push af')
    return output