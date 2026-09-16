def output_pdf_plot(core_result, spid, models, options, fit_results):
    hist_bins = 11
    emp_hist, edges = np.histogram(core_result['y'].values, hist_bins,
        normed=True)
    x = (np.array(edges[:-1]) + np.array(edges[1:])) / 2
    df = pd.DataFrame({'x': x, 'empirical': emp_hist})

    def calc_func(model, df, shapes):
        try:
            return eval("mod.%s.pmf(np.floor(df['x']), *shapes)" % model)
        except:
            return eval("mod.%s.pdf(df['x'], *shapes)" % model)
    plot_exec_str = "ax.bar(df['x']-width/2, emp, width=width, color='gray')"
    _save_table_and_plot(spid, models, options, fit_results,
        'data_pred_pdf', df, calc_func, plot_exec_str)