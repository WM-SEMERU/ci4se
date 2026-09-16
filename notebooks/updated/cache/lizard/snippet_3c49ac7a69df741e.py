def generate_parameters(self, parameter_id):
    if self.first_one:
        init_challenger = self.smbo_solver.nni_smac_start()
        self.total_data[parameter_id] = init_challenger
        return self.convert_loguniform_categorical(init_challenger.
            get_dictionary())
    else:
        challengers = self.smbo_solver.nni_smac_request_challengers()
        for challenger in challengers:
            self.total_data[parameter_id] = challenger
            return self.convert_loguniform_categorical(challenger.
                get_dictionary())