def plotCastro(castroData, ylims, nstep=25, zlims=None):
    xlabel = 'Energy [MeV]'
    ylabel = NORM_LABEL[castroData.norm_type]
    return plotCastro_base(castroData, ylims, xlabel, ylabel, nstep, zlims)