def ding0_exemplary_plots(stats, base_path=BASEPATH):
    plotpath = os.path.join(base_path, 'plots')
    results.plot_cable_length(stats, plotpath)
    plt.show()
    results.plot_generation_over_load(stats, plotpath)
    plt.show()