def plot_covariance_ellipse(mean, cov=None, variance=1.0, std=None, ellipse
    =None, title=None, axis_equal=True, show_semiaxis=False, facecolor=None,
    edgecolor=None, fc='none', ec='#004080', alpha=1.0, xlim=None, ylim=
    None, ls='solid'):
    warnings.warn('deprecated, use plot_covariance instead', DeprecationWarning
        )
    plot_covariance(mean=mean, cov=cov, variance=variance, std=std, ellipse
        =ellipse, title=title, axis_equal=axis_equal, show_semiaxis=
        show_semiaxis, facecolor=facecolor, edgecolor=edgecolor, fc=fc, ec=
        ec, alpha=alpha, xlim=xlim, ylim=ylim, ls=ls)