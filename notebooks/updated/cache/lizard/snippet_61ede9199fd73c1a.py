def suggest_next_locations(self, context=None, pending_X=None, ignored_X=None):
    self.model_parameters_iterations = None
    self.num_acquisitions = 0
    self.context = context
    self._update_model(self.normalization_type)
    suggested_locations = self._compute_next_evaluations(pending_zipped_X=
        pending_X, ignored_zipped_X=ignored_X)
    return suggested_locations