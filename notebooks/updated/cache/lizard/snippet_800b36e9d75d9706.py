def _gei8(ins):
    output = _8bit_oper(ins.quad[2], ins.quad[3], reversed_=True)
    output.append('call __LEI8')
    output.append('push af')
    REQUIRES.add('lei8.asm')
    return output