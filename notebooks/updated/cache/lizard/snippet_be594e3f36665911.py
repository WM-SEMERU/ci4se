def mark_fit_good(self, fit, spec=None):
    if spec == None:
        for spec, fits in list(self.pmag_results_data['specimens'].items()):
            if fit in fits:
                break
    samp = self.Data_hierarchy['sample_of_specimen'][spec]
    if 'sample_orientation_flag' not in self.Data_info['er_samples'][samp]:
        self.Data_info['er_samples'][samp]['sample_orientation_flag'] = 'g'
    samp_flag = self.Data_info['er_samples'][samp]['sample_orientation_flag']
    if samp_flag == 'g':
        self.bad_fits.remove(fit)
        return True
    else:
        self.user_warning(
            'Cannot mark this interpretation good its sample orientation has been marked bad'
            )
        return False