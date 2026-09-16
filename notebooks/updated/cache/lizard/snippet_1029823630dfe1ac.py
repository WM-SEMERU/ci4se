def to_fixed(stype):
    output = []
    if is_int_type(stype):
        output = to_word(stype)
        output.append('ex de, hl')
        output.append('ld hl, 0')
    elif stype == 'f':
        output.append('call __FTOF16REG')
        REQUIRES.add('ftof16reg.asm')
    return output