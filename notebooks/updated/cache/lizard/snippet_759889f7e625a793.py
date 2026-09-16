def _lei16(ins):
    output = _16bit_oper(ins.quad[2], ins.quad[3])
    output.append('call __LEI16')
    output.append('push af')
    REQUIRES.add('lei16.asm')
    return output