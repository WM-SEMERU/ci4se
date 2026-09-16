def _check_lsm_input(self, data_var_map_array):
    REQUIRED_HMET_VAR_LIST = ['Prcp', 'Pres', 'Temp', 'Clod', 'RlHm',
        'Drad', 'Grad', 'WndS']
    given_hmet_var_list = []
    for gssha_data_var, lsm_data_var in data_var_map_array:
        gssha_data_hmet_name = self.netcdf_attributes[gssha_data_var][
            'hmet_name']
        if gssha_data_hmet_name in given_hmet_var_list:
            raise ValueError('Duplicate parameter for HMET variable {0}'.
                format(gssha_data_hmet_name))
        else:
            given_hmet_var_list.append(gssha_data_hmet_name)
    for REQUIRED_HMET_VAR in REQUIRED_HMET_VAR_LIST:
        if REQUIRED_HMET_VAR not in given_hmet_var_list:
            raise ValueError(
                'ERROR: HMET param is required to continue {0} ...'.format(
                REQUIRED_HMET_VAR))