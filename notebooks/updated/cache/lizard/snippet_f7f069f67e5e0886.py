def sca_xsect(scatterer, h_pol=True):
    if scatterer.psd_integrator is not None:
        return scatterer.psd_integrator.get_angular_integrated(scatterer.
            psd, scatterer.get_geometry(), 'sca_xsect')
    old_geom = scatterer.get_geometry()

    def d_xsect(thet, phi):
        scatterer.phi, scatterer.thet = phi * rad_to_deg, thet * rad_to_deg
        Z = scatterer.get_Z()
        I = sca_intensity(scatterer, h_pol)
        return I * np.sin(thet)
    try:
        xsect = dblquad(d_xsect, 0.0, 2 * np.pi, lambda x: 0.0, lambda x: np.pi
            )[0]
    finally:
        scatterer.set_geometry(old_geom)
    return xsect