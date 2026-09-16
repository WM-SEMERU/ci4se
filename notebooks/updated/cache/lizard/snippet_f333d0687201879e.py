def get_PCA_parameters(self, specimen, fit, tmin, tmax, coordinate_system,
    calculation_type):
    if tmin == '' or tmax == '':
        return
    beg_pca, end_pca = self.get_indices(fit, tmin, tmax, specimen)
    if coordinate_system == 'geographic' or coordinate_system == 'DA-DIR-GEO':
        block = self.Data[specimen]['zijdblock_geo']
    elif coordinate_system == 'tilt-corrected' or coordinate_system == 'DA-DIR-TILT':
        block = self.Data[specimen]['zijdblock_tilt']
    else:
        block = self.Data[specimen]['zijdblock']
    if block == []:
        print(
            '-E- no measurement data for specimen %s in coordinate system %s' %
            (specimen, coordinate_system))
        mpars = {}
    elif end_pca > beg_pca and end_pca - beg_pca > 1:
        try:
            mpars = pmag.domean(block, beg_pca, end_pca, calculation_type)
        except:
            print((block, beg_pca, end_pca, calculation_type, specimen, fit
                .name, tmin, tmax, coordinate_system))
            return
        if 'specimen_direction_type' in mpars and mpars[
            'specimen_direction_type'] == 'Error':
            print(
                '-E- no measurement data for specimen %s in coordinate system %s'
                 % (specimen, coordinate_system))
            return {}
    else:
        mpars = {}
    for k in list(mpars.keys()):
        try:
            if math.isnan(float(mpars[k])):
                mpars[k] = 0
        except:
            pass
    if 'DE-BFL' in calculation_type and 'specimen_dang' not in list(mpars.
        keys()):
        mpars['specimen_dang'] = 0
    if 'best fit vector' in self.plane_display_box.GetValue():
        self.calculate_best_fit_vectors()
    return mpars