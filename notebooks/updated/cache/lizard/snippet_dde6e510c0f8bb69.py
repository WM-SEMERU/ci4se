def _regressor_names(con_name, hrf_model, fir_delays=None):
    if hrf_model in ['glover', 'spm', None]:
        return [con_name]
    elif hrf_model in ['glover + derivative', 'spm + derivative']:
        return [con_name, con_name + '_derivative']
    elif hrf_model in ['spm + derivative + dispersion',
        'glover + derivative + dispersion']:
        return [con_name, con_name + '_derivative', con_name + '_dispersion']
    elif hrf_model == 'fir':
        return [(con_name + '_delay_%d' % i) for i in fir_delays]