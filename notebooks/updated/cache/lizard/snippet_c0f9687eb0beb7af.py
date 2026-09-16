def solar_spectrum(model='SOLAR-ISS'):
    r
    if model == 'SOLAR-ISS':
        pth = os.path.join(folder, 'solar_iss_2018_spectrum.dat')
        data = np.loadtxt(pth)
        wavelengths, SSI, uncertainties = data[:, (0)], data[:, (1)], data[:,
            (2)]
        wavelengths = wavelengths * 1e-09
        SSI = SSI * 1000000000.0
        uncertainties[uncertainties == -1] = np.nan
        uncertainties = uncertainties * 1000000000.0
    return wavelengths, SSI, uncertainties