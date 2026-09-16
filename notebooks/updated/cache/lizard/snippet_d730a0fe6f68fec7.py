def update_PCA_box(self):
    if self.s in list(self.pmag_results_data['specimens'].keys()):
        if self.current_fit:
            tmin = self.current_fit.tmin
            tmax = self.current_fit.tmax
            calculation_type = self.current_fit.PCA_type
        else:
            calculation_type = self.PCA_type_box.GetValue()
            PCA_type = 'None'
        if calculation_type == 'DE-BFL':
            PCA_type = 'line'
        elif calculation_type == 'DE-BFL-A':
            PCA_type = 'line-anchored'
        elif calculation_type == 'DE-BFL-O':
            PCA_type = 'line-with-origin'
        elif calculation_type == 'DE-FM':
            PCA_type = 'Fisher'
        elif calculation_type == 'DE-BFP':
            PCA_type = 'plane'
        else:
            print('no PCA type found setting to line')
            PCA_type = 'line'
        self.PCA_type_box.SetStringSelection(PCA_type)