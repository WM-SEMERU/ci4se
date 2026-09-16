def plot_skyreg(header, data, **kwargs):
    kwargs.setdefault('cmap', 'binary')
    fig = plt.figure()
    ax = pywcsgrid2.subplot(111, header=header)
    ax.set_ticklabel_type('dms')
    im = ax.imshow(data, origin='center', **kwargs)
    ax.grid()
    ax.add_compass(loc=1, coord='fk5')
    ax.add_compass(loc=4, coord='gal')
    return ax, im