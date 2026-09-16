def imshow_z(data, name):
    zmes = pick_flat_z(data)
    plt.figure()
    plt.imshow(zmes.T, origin='lower', extent=[data['doping'].min(), data[
        'doping'].max(), 0, data['u_int'].max()], aspect=0.16)
    plt.colorbar()
    plt.xlabel('$n$', fontsize=20)
    plt.ylabel('$U/D$', fontsize=20)
    plt.savefig(name + '_imshow.png', dpi=300, format='png', transparent=
        False, bbox_inches='tight', pad_inches=0.05)