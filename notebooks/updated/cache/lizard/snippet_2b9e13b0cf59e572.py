def abup_se_plot(mod, species):
    species = 'C-12'
    filename = 'ABUPP%07d0000.DAT' % mod
    print(filename)
    mass, c12 = np.loadtxt(filename, skiprows=4, usecols=[1, 18], unpack=True)
    c12_se = self.se.get(mod, 'iso_massf', 'C-12')
    mass_se = self.se.get(mod, 'mass')
    pyl.plot(mass, c12)
    pyl.plot(mass_se, c12_se, 'o', label='cycle ' + str(mod))
    pyl.legend()