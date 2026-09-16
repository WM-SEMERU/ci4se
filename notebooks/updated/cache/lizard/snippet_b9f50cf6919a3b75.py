def create_tdplot(plotman, cov, mag, pha, pha_fpi, alpha, options):
    sizex, sizez = getfigsize(plotman)
    f, ax = plt.subplots(2, 4, figsize=(4 * sizex, 2 * sizez))
    if options.title is not None:
        plt.suptitle(options.title, fontsize=18)
    if options.cmaglin:
        cid = plotman.parman.add_data(np.power(10, mag))
        loglin = 'rho'
    else:
        cid = plotman.parman.add_data(mag)
        loglin = 'log_rho'
    plot_mag(cid, ax[0, 0], plotman, 'Magnitude', loglin, alpha, options.
        mag_vmin, options.mag_vmax, options.xmin, options.xmax, options.
        zmin, options.zmax, options.unit, options.mag_cbtiks, options.no_elecs)
    cid = plotman.parman.add_data(cov)
    plot_cov(cid, ax[1, 0], plotman, 'Coverage', options.cov_vmin, options.
        cov_vmax, options.xmin, options.xmax, options.zmin, options.zmax,
        options.unit, options.cov_cbtiks, options.no_elecs)
    create_non_dcplots(plotman, ax, mag, pha, options, alpha)
    create_fpiplots(plotman, ax, mag, pha_fpi, options, alpha)
    f.tight_layout()
    f.savefig('td_overview.png', dpi=300)
    return f, ax