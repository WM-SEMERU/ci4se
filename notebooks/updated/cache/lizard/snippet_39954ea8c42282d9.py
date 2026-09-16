def encode_mv(vals):
    s = ''
    for val in vals:
        val = val.replace('$', '$$')
        if len(s) > 0:
            s += ';'
        s += '$' + val + '$'
    return s