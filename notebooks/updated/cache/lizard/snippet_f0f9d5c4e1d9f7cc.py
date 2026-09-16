def get_partial_doses(self, tdos, npts_mu, T):
    spin = self.data.spin if isinstance(self.data.spin, int) else 1
    if not isinstance(self.data.proj, np.ndarray):
        raise BoltztrapError('No projections loaded.')
    bkp_data_ebands = np.copy(self.data.ebands)
    pdoss = {}
    for isite, site in enumerate(self.data.structure.sites):
        if site not in pdoss:
            pdoss[site] = {}
        for iorb, orb in enumerate(Orbital):
            if iorb == self.data.proj.shape[-1]:
                break
            if orb not in pdoss[site]:
                pdoss[site][orb] = {}
            self.data.ebands = self.data.proj[:, :, (isite), (iorb)].T
            coeffs = fite.fitde3D(self.data, self.equivalences)
            proj, vvproj, cproj = fite.getBTPbands(self.equivalences,
                coeffs, self.data.lattvec)
            edos, pdos = BL.DOS(self.eband, npts=npts_mu, weights=np.abs(
                proj.real))
            if T is not None:
                pdos = BL.smoothen_DOS(edos, pdos, T)
            pdoss[site][orb][Spin(spin)] = pdos
    self.data.ebands = bkp_data_ebands
    return CompleteDos(self.data.structure, total_dos=tdos, pdoss=pdoss)