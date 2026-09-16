def plotpsd(data, dt, ndivide=1, window=hanning, overlap_half=False, ax=
    None, **kwargs):
    if ax is None:
        ax = plt.gca()
    vk, psddata = psd(data, dt, ndivide, window, overlap_half)
    ax.loglog(vk, psddata, **kwargs)
    ax.set_xlabel('Frequency [Hz]')
    ax.set_ylabel('PSD')
    ax.legend()