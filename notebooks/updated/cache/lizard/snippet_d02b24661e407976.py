def _handle_author(author):
    lname = author.split(' ')
    try:
        auinit = lname[0][0]
        final = lname[-1].upper()
        if final in ['JR.', 'III']:
            aulast = lname[-2].upper() + ' ' + final.strip('.')
        else:
            aulast = final
    except IndexError:
        raise ValueError('malformed author name')
    return aulast, auinit