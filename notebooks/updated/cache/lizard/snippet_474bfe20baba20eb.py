def gaussian_prior_model_for_arguments(self, arguments):
    new_model = copy.deepcopy(self)
    model_arguments = {t.name: arguments[t.prior] for t in self.
        direct_prior_tuples}
    for tuple_prior_tuple in self.tuple_prior_tuples:
        setattr(new_model, tuple_prior_tuple.name, tuple_prior_tuple.prior.
            gaussian_tuple_prior_for_arguments(arguments))
    for prior_tuple in self.direct_prior_tuples:
        setattr(new_model, prior_tuple.name, model_arguments[prior_tuple.name])
    for constant_tuple in self.constant_tuples:
        setattr(new_model, constant_tuple.name, constant_tuple.constant)
    for name, prior_model in self.direct_prior_model_tuples:
        setattr(new_model, name, prior_model.
            gaussian_prior_model_for_arguments(arguments))
    return new_model