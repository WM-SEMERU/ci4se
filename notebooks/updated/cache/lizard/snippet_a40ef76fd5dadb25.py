def extract(data, defs, byteoffset=0):
    retval = ListDict()
    for fielddef in defs:
        start, width, form, name, desc = fielddef
        if form == 'int':
            if type(start) == type(0):
                start = start, 7
            ix, bitnum = start
            val = 0
            while width > 0:
                if bitnum == 7 and width >= 8:
                    val = val << 8 | ord(data[ix])
                    ix += 1
                    width -= 8
                else:
                    lastbit = bitnum + 1 - width
                    if lastbit < 0:
                        lastbit = 0
                    thiswidth = bitnum + 1 - lastbit
                    val = val << thiswidth | ord(data[ix]) >> lastbit & (1 <<
                        thiswidth) - 1
                    bitnum = 7
                    ix += 1
                    width -= thiswidth
            retval.append(Cmd.Field(val, byteoffset + start[0], name, desc),
                name)
        elif form == 'str':
            assert type(start) == type(0)
            assert width % 8 == 0
            retval.append(Cmd.Field(data[start:start + width / 8], 
                byteoffset + start, name, desc), name)
        else:
            pass
    return retval