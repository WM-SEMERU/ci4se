def classifyplot_from_plotfiles(plot_files, out_csv, outtype='png', title=
    None, size=None):
    dfs = [pd.read_csv(x) for x in plot_files]
    samples = []
    for df in dfs:
        for sample in df['sample'].unique():
            if sample not in samples:
                samples.append(sample)
    df = pd.concat(dfs)
    df.to_csv(out_csv, index=False)
    return classifyplot_from_valfile(out_csv, outtype, title, size, samples)