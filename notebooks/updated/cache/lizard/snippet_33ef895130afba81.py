def plot_seebeck_mu(self, temp=600, output='eig', xlim=None):
    import matplotlib.pyplot as plt
    plt.figure(figsize=(9, 7))
    seebeck = self._bz.get_seebeck(output=output, doping_levels=False)[temp]
    plt.plot(self._bz.mu_steps, seebeck, linewidth=3.0)
    self._plot_bg_limits()
    self._plot_doping(temp)
    if output == 'eig':
        plt.legend(['S$_1$', 'S$_2$', 'S$_3$'])
    if xlim is None:
        plt.xlim(-0.5, self._bz.gap + 0.5)
    else:
        plt.xlim(xlim[0], xlim[1])
    plt.ylabel('Seebeck \n coefficient  ($\\mu$V/K)', fontsize=30.0)
    plt.xlabel('E-E$_f$ (eV)', fontsize=30)
    plt.xticks(fontsize=25)
    plt.yticks(fontsize=25)
    plt.tight_layout()
    return plt