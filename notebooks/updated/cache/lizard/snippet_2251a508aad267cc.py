def BMI(self, params):
    label = self.get_one_parameter(self.ONE_PARAMETER, params)
    self.check_arguments(label_exists=(label,))

    def BMI_func():
        if self.is_N_set():
            self.register['PC'] = self.labels[label]
    return BMI_func