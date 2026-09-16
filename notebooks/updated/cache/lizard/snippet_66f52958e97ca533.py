def plot_triaxial_depths_speed(tag):
    import numpy
    from . import plotutils
    fig, axes = plt.subplots(3, 3, sharex='col', sharey='row')
    (ax1, ax4, ax7), (ax2, ax5, ax8), (ax3, ax6, ax9) = axes
    all_ind = numpy.arange(0, len(tag), dtype=int)
    cols = [('x', tag['Ax_g'], [ax1, ax2, ax3]), ('y', tag['Ay_g'], [ax4,
        ax5, ax6]), ('z', tag['Az_g'], [ax7, ax8, ax9])]
    for label, y, axes in cols:
        axes[0].title.set_text('Accelerometer {}-axis'.format(label))
        axes[0].plot(range(len(y)), y, color=_colors[0], linewidth=
            _linewidth, label='x')
        axes[1].title.set_text('Depths')
        axes[1] = plotutils.plot_noncontiguous(axes[1], tag['depth'],
            all_ind, color=_colors[1])
        axes[1].invert_yaxis()
        axes[2] = plotutils.plot_noncontiguous(axes[2], tag['propeller'],
            all_ind, color=_colors[2], label='propeller')
    plt.show()
    return None