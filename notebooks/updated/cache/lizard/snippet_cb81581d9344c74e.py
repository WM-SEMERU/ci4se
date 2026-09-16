def get_best_fit_parameters_translated_grouped(self):
    result_dict = dict()
    result_dict['ocv'] = [parameters['ocv'] for parameters in self.
        best_fit_parameters_translated]
    result_dict['ir'] = [parameters['ir'] for parameters in self.
        best_fit_parameters_translated]
    for i in range(self.circuits):
        result_dict['r' + str(i)] = [parameters['r' + str(i)] for
            parameters in self.best_fit_parameters_translated]
        result_dict['c' + str(i)] = [parameters['c' + str(i)] for
            parameters in self.best_fit_parameters_translated]
    return result_dict