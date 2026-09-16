def plot_results(fout_png, goea_results, *args, **kws):
    if '{NS}' not in fout_png:
        plt_goea_results(fout_png, goea_results, *args, **kws)
    else:
        ns2goea_results = cx.defaultdict(list)
        for rec in goea_results:
            ns2goea_results[rec.NS].append(rec)
        for ns_name, ns_res in ns2goea_results.items():
            png = fout_png.format(NS=ns_name)
            plt_goea_results(png, ns_res, *args, **kws)