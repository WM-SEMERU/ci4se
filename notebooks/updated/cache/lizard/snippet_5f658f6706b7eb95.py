def _jzerostr(ins):
    output = []
    disposable = False
    if ins.quad[1][0] == '_':
        output.append('ld hl, (%s)' % ins.quad[1][0])
    else:
        output.append('pop hl')
        output.append('push hl')
        disposable = True
    output.append('call __STRLEN')
    if disposable:
        output.append('ex (sp), hl')
        output.append('call __MEM_FREE')
        output.append('pop hl')
        REQUIRES.add('alloc.asm')
    output.append('ld a, h')
    output.append('or l')
    output.append('jp z, %s' % str(ins.quad[2]))
    REQUIRES.add('strlen.asm')
    return output