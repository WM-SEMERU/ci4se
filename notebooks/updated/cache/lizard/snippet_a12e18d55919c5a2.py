def drawMask(self, ax=None, mask=None, mtype='maglim'):
    if not ax:
        ax = plt.gca()
    if mask is None:
        mask = ugali.analysis.loglike.createMask(self.config, roi=self.roi)
    mask_map = hp.UNSEEN * np.ones(hp.nside2npix(self.nside))
    if mtype.lower() == 'maglim':
        mask_map[mask.roi.pixels] = mask.mask_1.mask_roi_sparse
    elif mtype.lower() == 'fracdet':
        mask_map[mask.roi.pixels] = mask.mask_1.frac_roi_sparse
    else:
        raise Exception('Unrecognized type: %s' % mtype)
    masked = (mask_map == hp.UNSEEN) | (mask_map == 0)
    mask_map = np.ma.array(mask_map, mask=masked, fill_value=np.nan)
    im = drawHealpixMap(mask_map, self.lon, self.lat, self.radius, coord=
        self.coord)
    try:
        cbar = ax.cax.colorbar(im)
    except:
        cbar = plt.colorbar(im)
    cbar.ax.set_xticklabels(cbar.ax.get_xticklabels(), rotation=90)
    ax.annotate(mtype, **self.label_kwargs)
    return im