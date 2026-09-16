def _get_input_to_checker_function(self, flag_values):
    return dict([key, flag_values[key].value] for key in self.flag_names)