def fits_list(filter, root, fnames):
    import re, pyfits, wcsutil
    for file in fnames:
        if re.match(filter, file):
            fh = pyfits.open(file)
            for ext in fh:
                obj = ext.header.get('OBJECT', file)
                dx = ext.header.get('NAXIS1', None)
                dy = ext.header.get('NAXIS2', None)
                wcs = wcsutil.WCSObject(ext)
                x1, y1 = wcs.xy2rd((1, 1))
                x2, y2 = wcs.xy2rd((dx, dy))
                ccds = [x1, y1, x2, y2]
                pointing = {'label': obj, 'camera': ccds}
    return files