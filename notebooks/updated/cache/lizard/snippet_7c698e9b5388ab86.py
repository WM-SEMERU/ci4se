def time_plots(df, path, title=None, color='#4CB391', figformat='png',
    log_length=False, plot_settings=None):
    dfs = check_valid_time_and_sort(df, 'start_time')
    logging.info('Nanoplotter: Creating timeplots using {} reads.'.format(
        len(dfs)))
    cumyields = cumulative_yield(dfs=dfs.set_index('start_time'), path=path,
        figformat=figformat, title=title, color=color)
    reads_pores_over_time = plot_over_time(dfs=dfs.set_index('start_time'),
        path=path, figformat=figformat, title=title, color=color)
    violins = violin_plots_over_time(dfs=dfs, path=path, figformat=
        figformat, title=title, log_length=log_length, plot_settings=
        plot_settings)
    return cumyields + reads_pores_over_time + violins