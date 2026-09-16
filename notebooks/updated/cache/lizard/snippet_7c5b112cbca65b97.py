def plot_zeropoint(pars):
    from matplotlib import pyplot as plt
    xp = pars['xp']
    yp = pars['yp']
    searchrad = int(pars['searchrad'] + 0.5)
    plt.figure(num=pars['figure_id'])
    plt.clf()
    if pars['interactive']:
        plt.ion()
    else:
        plt.ioff()
    plt.imshow(pars['data'], vmin=0, vmax=pars['vmax'], interpolation='nearest'
        )
    plt.viridis()
    plt.colorbar()
    plt.title(pars['title_str'])
    plt.plot(xp + searchrad, yp + searchrad, color='red', marker='+',
        markersize=24)
    plt.plot(searchrad, searchrad, color='yellow', marker='+', markersize=120)
    plt.text(searchrad, searchrad, 'Offset=0,0', verticalalignment='bottom',
        color='yellow')
    plt.xlabel('Offset in X (pixels)')
    plt.ylabel('Offset in Y (pixels)')
    if pars['interactive']:
        plt.show()
    if pars['plotname']:
        suffix = pars['plotname'][-4:]
        output = pars['plotname']
        if '.' not in suffix:
            output += '.png'
            format = 'png'
        elif suffix[1:] in ['png', 'pdf', 'ps', 'eps', 'svg']:
            format = suffix[1:]
        plt.savefig(output, format=format)