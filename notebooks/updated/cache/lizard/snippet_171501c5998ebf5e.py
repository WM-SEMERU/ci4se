def get_astheader(expnum, ccd, version='p', prefix=None):
    logger.debug('Getting ast header for {}'.format(expnum))
    if version == 'p':
        try:
            sg_key = '{}{}'.format(expnum, version)
            if sg_key not in sgheaders:
                _get_sghead(expnum)
            if sg_key in sgheaders:
                for header in sgheaders[sg_key]:
                    if header.get('EXTVER', -1) == int(ccd):
                        return header
        except:
            pass
    try:
        ast_uri = dbimages_uri(expnum, ccd, version=version, ext='.fits')
        if ast_uri not in astheaders:
            hdulist = get_image(expnum, ccd=ccd, version=version, prefix=
                prefix, cutout='[1:1,1:1]', return_file=False, ext='.fits')
            assert isinstance(hdulist, fits.HDUList)
            astheaders[ast_uri] = hdulist[0].header
    except:
        ast_uri = dbimages_uri(expnum, ccd, version=version, ext='.fits.fz')
        if ast_uri not in astheaders:
            hdulist = get_image(expnum, ccd=ccd, version=version, prefix=
                prefix, cutout='[1:1,1:1]', return_file=False, ext='.fits.fz')
            assert isinstance(hdulist, fits.HDUList)
            astheaders[ast_uri] = hdulist[0].header
    return astheaders[ast_uri]