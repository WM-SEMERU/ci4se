def unpack_di_block(di_block):
    dec_list = []
    inc_list = []
    moment_list = []
    for n in range(0, len(di_block)):
        dec = di_block[n][0]
        inc = di_block[n][1]
        dec_list.append(dec)
        inc_list.append(inc)
        if len(di_block[n]) > 2:
            moment = di_block[n][2]
            moment_list.append(moment)
    return dec_list, inc_list, moment_list