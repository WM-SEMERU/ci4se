def xcorr_plot(template, image, shift=None, cc=None, cc_vec=None, **kwargs):
    import matplotlib.pyplot as plt
    if cc is None or shift is None:
        if not isinstance(cc_vec, np.ndarray):
            print('Given cc: %s and shift: %s' % (cc, shift))
            raise IOError('Must provide either cc_vec, or cc and shift')
        shift = np.abs(cc_vec).argmax()
        cc = cc_vec[shift]
    x = np.arange(len(image))
    plt.plot(x, image / abs(image).max(), 'k', lw=1.3, label='Image')
    x = np.arange(len(template)) + shift
    plt.plot(x, template / abs(template).max(), 'r', lw=1.1, label='Template')
    plt.title('Shift=%s, Correlation=%s' % (shift, cc))
    fig = plt.gcf()
    fig = _finalise_figure(fig=fig, **kwargs)
    return fig