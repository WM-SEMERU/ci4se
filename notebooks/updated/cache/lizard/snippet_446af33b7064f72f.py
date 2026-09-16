def generate_headerlet(outwcs, template, wcsname, outname=None):
    siphdr = True
    if outwcs.sip is None:
        siphdr = False
    outwcs_hdr = outwcs.wcs2header(sip2hdr=siphdr)
    outwcs_hdr['NPIX1'] = outwcs.pixel_shape[0]
    outwcs_hdr['NPIX2'] = outwcs.pixel_shape[1]
    if template is not None and siphdr:
        print('Creating headerlet from template...')
        fname, extn = fileutil.parseFilename(template)
        extnum = fileutil.parseExtn(extn)
        extname = 'sipwcs', extnum[1]
        hdrlet = headerlet.createHeaderlet(fname, wcsname)
        for kw in outwcs_hdr.items():
            hdrlet[extname].header[kw[0]] = kw[1]
        hdrlet[extname].header['WCSNAME'] = wcsname
    else:
        print('Creating headerlet from scratch...')
        hdrlet = fits.HDUList()
        hdrlet.append(fits.PrimaryHDU())
        siphdr = fits.ImageHDU(header=outwcs_hdr)
        siphdr.header['EXTNAME'] = 'SIPWCS'
        siphdr.header['WCSNAME'] = wcsname
        hdrlet.append(siphdr)
    if outname is not None:
        if outname.find('_hdr.fits') < 0:
            outname += '_hdr.fits'
        if os.path.exists(outname):
            print('Overwrite existing file "%s"' % outname)
            os.remove(outname)
        hdrlet.writeto(outname)
        print('Wrote out headerlet :', outname)