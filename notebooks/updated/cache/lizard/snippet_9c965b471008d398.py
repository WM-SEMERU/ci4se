def superpixel(subpix, nside_subpix, nside_superpix):
    if nside_subpix == nside_superpix:
        return subpix
    theta, phi = hp.pix2ang(nside_subpix, subpix)
    return hp.ang2pix(nside_superpix, theta, phi)