def _extra_regression_kwargs(self):
    omega_switch_test = 0.019
    extra_args = []
    extra_args.append({'omega0': 0.005, 'PN_approximant': 'SpinTaylorT4',
        'PN_dt': 0.1, 'PN_spin_order': 7, 'PN_phase_order': 7,
        'omega_switch': omega_switch_test})
    extra_args.append({'omega0': 0.006, 'PN_approximant': 'SpinTaylorT1',
        'PN_dt': 0.5, 'PN_spin_order': 5, 'PN_phase_order': 7,
        'omega_switch': omega_switch_test})
    extra_args.append({'omega0': 0.007, 'PN_approximant': 'SpinTaylorT2',
        'PN_dt': 1, 'PN_spin_order': 7, 'PN_phase_order': 5, 'omega_switch':
        omega_switch_test})
    extra_args.append({'omega0': 0.03})
    extra_args.append({'omega0': 0.05})
    return extra_args