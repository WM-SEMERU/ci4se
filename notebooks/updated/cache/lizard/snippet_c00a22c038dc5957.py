def _get_stddevs(self, C, C_PGA, rup, sites, pga1100, stddev_types):
    tau_lnpga_b, phi_lnpga_b = self._get_stddevs_pga(C_PGA, rup)
    num_sites = len(sites.vs30)
    tau_lnyb = self._get_taulny(C, rup.mag)
    phi_lnyb = np.sqrt(self._get_philny(C, rup.mag) ** 2.0 - self.CONSTS[
        'philnAF'] ** 2.0)
    alpha = self._get_alpha(C, sites.vs30, pga1100)
    tau = np.sqrt(tau_lnyb ** 2.0 + alpha ** 2.0 * tau_lnpga_b ** 2.0 + 2.0 *
        alpha * C['rholny'] * tau_lnyb * tau_lnpga_b)
    phi = np.sqrt(phi_lnyb ** 2.0 + self.CONSTS['philnAF'] ** 2.0 + alpha **
        2.0 * phi_lnpga_b ** 2.0 + 2.0 * alpha * C['rholny'] * phi_lnyb *
        phi_lnpga_b)
    stddevs = []
    for stddev_type in stddev_types:
        assert stddev_type in self.DEFINED_FOR_STANDARD_DEVIATION_TYPES
        if stddev_type == const.StdDev.TOTAL:
            stddevs.append(np.sqrt(tau ** 2.0 + phi ** 2.0) + np.zeros(
                num_sites))
        elif stddev_type == const.StdDev.INTRA_EVENT:
            stddevs.append(phi + np.zeros(num_sites))
        elif stddev_type == const.StdDev.INTER_EVENT:
            stddevs.append(tau + np.zeros(num_sites))
    return stddevs