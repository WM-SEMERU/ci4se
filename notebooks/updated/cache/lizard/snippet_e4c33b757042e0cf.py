def get_feature_variable_double(self, feature_key, variable_key, user_id,
    attributes=None):
    variable_type = entities.Variable.Type.DOUBLE
    return self._get_feature_variable_for_type(feature_key, variable_key,
        variable_type, user_id, attributes)