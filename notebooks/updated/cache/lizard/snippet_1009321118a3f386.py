def _ploadstr(ins):
    output = _pload(ins.quad[2], 2)
    if ins.quad[1][0] != '$':
        output.append('call __LOADSTR')
        REQUIRES.add('loadstr.asm')
    output.append('push hl')
    return output