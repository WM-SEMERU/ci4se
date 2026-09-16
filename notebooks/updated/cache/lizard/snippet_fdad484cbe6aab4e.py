def recalculate_current_specimen_interpreatations(self):
    self.initialize_CART_rot(self.s)
    if str(self.s) in self.pmag_results_data['specimens']:
        for fit in self.pmag_results_data['specimens'][self.s]:
            if fit.get('specimen') and 'calculation_type' in fit.get('specimen'
                ):
                fit.put(self.s, 'specimen', self.get_PCA_parameters(self.s,
                    fit, fit.tmin, fit.tmax, 'specimen', fit.get('specimen'
                    )['calculation_type']))
            if len(self.Data[self.s]['zijdblock_geo']) > 0 and fit.get(
                'geographic') and 'calculation_type' in fit.get('geographic'):
                fit.put(self.s, 'geographic', self.get_PCA_parameters(self.
                    s, fit, fit.tmin, fit.tmax, 'geographic', fit.get(
                    'geographic')['calculation_type']))
            if len(self.Data[self.s]['zijdblock_tilt']) > 0 and fit.get(
                'tilt-corrected') and 'calculation_type' in fit.get(
                'tilt-corrected'):
                fit.put(self.s, 'tilt-corrected', self.get_PCA_parameters(
                    self.s, fit, fit.tmin, fit.tmax, 'tilt-corrected', fit.
                    get('tilt-corrected')['calculation_type']))