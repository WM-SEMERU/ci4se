def verifyRefimage(refimage):
    valid = True
    if is_blank(refimage):
        valid = True
        return valid
    refroot, extroot = fileutil.parseFilename(refimage)
    if not os.path.exists(refroot):
        valid = False
        return valid
    if valid:
        if extroot is None:
            extn = findWCSExtn(refimage)
            if extn is None:
                valid = False
            else:
                valid = True
        else:
            refwcs = wcsutil.HSTWCS(refimage)
            if not refwcs.wcs.has_cd():
                valid = False
            else:
                valid = True
            del refwcs
    return valid