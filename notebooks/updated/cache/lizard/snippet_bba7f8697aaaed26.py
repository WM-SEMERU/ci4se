def _validate_resources(self):
    resources = self.options.resources
    for key in ['num_machines', 'num_mpiprocs_per_machine', 'tot_num_mpiprocs'
        ]:
        if key in resources and resources[key] != 1:
            raise exceptions.FeatureNotAvailable(
                "Cannot set resource '{}' to value '{}' for {}: parallelization is not supported, only a value of '1' is accepted."
                .format(key, resources[key], self.__class__.__name__))