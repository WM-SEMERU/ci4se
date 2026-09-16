def get_raw_limits(self):
    warnings.warn('raw limits have not been subject for testing yet')
    raw_limits = dict()
    raw_limits['current_hard'] = 0.1
    raw_limits['current_soft'] = 1.0
    raw_limits['stable_current_hard'] = 2.0
    raw_limits['stable_current_soft'] = 4.0
    raw_limits['stable_voltage_hard'] = 2.0
    raw_limits['stable_voltage_soft'] = 4.0
    raw_limits['stable_charge_hard'] = 2.0
    raw_limits['stable_charge_soft'] = 5.0
    raw_limits['ir_change'] = 1e-05
    return raw_limits