def J(self, log_sigma):
    m = 1.0 / np.exp(log_sigma)
    tdm = self._get_tdm(m)
    tdm.model(sensitivities=True)
    measurements = tdm.measurements()
    sens_list = []
    for config_nr, cids in sorted(tdm.assignments['sensitivities'].items()):
        sens_list.append(tdm.parman.parsets[cids[0]])
    sensitivities_lin = np.array(sens_list)
    sensitivities_log = sensitivities_lin
    measurements_rep = np.repeat(measurements[:, (0), (np.newaxis)],
        sensitivities_lin.shape[1], axis=1)
    m_rep = np.repeat(m[(np.newaxis), :], sensitivities_lin.shape[0], axis=0)
    factor = -1 / (m_rep * measurements_rep)
    sensitivities_log = factor * sensitivities_lin
    return sensitivities_log