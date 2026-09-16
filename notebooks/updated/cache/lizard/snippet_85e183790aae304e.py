def write_shiftfile(image_list, filename, outwcs='tweak_wcs.fits'):
    rows = ''
    nrows = 0
    for img in image_list:
        row = img.get_shiftfile_row()
        if row is not None:
            rows += row
            nrows += 1
    if nrows == 0:
        return
    if os.path.exists(outwcs):
        os.remove(outwcs)
    p = fits.HDUList()
    p.append(fits.PrimaryHDU())
    p.append(createWcsHDU(image_list[0].refWCS))
    p.writeto(outwcs)
    with open(filename, 'w') as f:
        f.write('# frame: output\n')
        f.write('# refimage: %s[wcs]\n' % outwcs)
        f.write('# form: delta\n')
        f.write('# units: pixels\n')
        f.write(rows)
    print('Writing out shiftfile :', filename)