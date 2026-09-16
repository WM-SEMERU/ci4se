def reference_pix_from_wcs_imgs(imgs, pixref, origin=1):
    result = []
    refimg = imgs[0]
    wcsh = wcs.WCS(refimg[0].header)
    skyref = wcsh.wcs_pix2world([pixref], origin)
    result.append(pixref)
    for idx, img in enumerate(imgs[1:]):
        wcsh = wcs.WCS(img[0].header)
        pixval = wcsh.wcs_world2pix(skyref, origin)
        result.append(tuple(pixval[0]))
    return result