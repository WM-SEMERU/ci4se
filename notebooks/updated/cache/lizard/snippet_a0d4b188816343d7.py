def prior_model_name_constant_tuples_dict(self):
    return {name: list(prior_model.constant_tuples) for name, prior_model in
        self.prior_model_tuples}