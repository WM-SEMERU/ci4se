def get_correction(self, entry):
    hybrid_cbm = entry.parameters['hybrid_cbm']
    hybrid_vbm = entry.parameters['hybrid_vbm']
    vbm = entry.parameters['vbm']
    cbm = entry.parameters['cbm']
    num_hole_vbm = entry.parameters['num_hole_vbm']
    num_elec_cbm = entry.parameters['num_elec_cbm']
    self.metadata['vbmshift'] = hybrid_vbm - vbm
    self.metadata['cbmshift'] = hybrid_cbm - cbm
    charge = entry.charge
    vbm_shift_correction = charge * self.metadata['vbmshift']
    hole_vbm_shift_correction = -1.0 * num_hole_vbm * self.metadata['vbmshift']
    elec_cbm_shift_correction = num_elec_cbm * self.metadata['cbmshift']
    entry.parameters['bandshift_meta'] = dict(self.metadata)
    return {'vbm_shift_correction': vbm_shift_correction,
        'hole_vbm_shift_correction': hole_vbm_shift_correction,
        'elec_cbm_shift_correction': elec_cbm_shift_correction}