def plot_2d_single(x, y, pdffilename, **kwargs):
    pdffilepath = DataSets.get_pdffilepath(pdffilename)
    plotsingle2d = PlotSingle2D(x, y, pdffilepath, **kwargs)
    return plotsingle2d.plot()