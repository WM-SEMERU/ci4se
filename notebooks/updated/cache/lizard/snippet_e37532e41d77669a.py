def replace_u(matchobj):
    pieces = list(matchobj.groups(''))
    if 'u' in pieces[1]:
        pieces[1] = pieces[1].replace('u', '0')
    if 'u' in pieces[5]:
        pieces[5] = pieces[5].replace('u', '9')
    if 'u' in pieces[2]:
        pieces[2] = '-' + replace_u_start_month(pieces[2])
    if 'u' in pieces[6]:
        pieces[6] = '-' + replace_u_end_month(pieces[6])
    if 'u' in pieces[3]:
        pieces[3] = '-' + replace_u_start_day(pieces[3])
    if 'u' in pieces[7]:
        pieces[7] = '-' + replace_u_end_day(pieces[7], year=pieces[5],
            month=pieces[6])
    return ''.join((''.join(pieces[:4]), '/', ''.join(pieces[4:])))