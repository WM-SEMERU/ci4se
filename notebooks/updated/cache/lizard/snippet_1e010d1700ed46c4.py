def countExtn(fimg, extname='SCI'):
    closefits = False
    if isinstance(fimg, string_types):
        fimg = fits.open(fimg)
        closefits = True
    n = 0
    for e in fimg:
        if 'extname' in e.header and e.header['extname'] == extname:
            n += 1
    if closefits:
        fimg.close()
    return n