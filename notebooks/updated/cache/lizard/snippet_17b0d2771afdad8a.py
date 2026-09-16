def get_rejected_variables(self, threshold=0.9):
    variable_profile = self.description_set['variables']
    result = []
    if hasattr(variable_profile, 'correlation'):
        result = variable_profile.index[variable_profile.correlation >
            threshold].tolist()
    return result