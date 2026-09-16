def instance_for_arguments(self, arguments: {Prior: float}):
    for prior, value in arguments.items():
        prior.assert_within_limits(value)
    model_arguments = {t.name: arguments[t.prior] for t in self.
        direct_prior_tuples}
    constant_arguments = {t.name: t.constant.value for t in self.
        direct_constant_tuples}
    for tuple_prior in self.tuple_prior_tuples:
        model_arguments[tuple_prior.name
            ] = tuple_prior.prior.value_for_arguments(arguments)
    for prior_model_tuple in self.direct_prior_model_tuples:
        model_arguments[prior_model_tuple.name
            ] = prior_model_tuple.prior_model.instance_for_arguments(arguments)
    return self.cls(**{**model_arguments, **constant_arguments})