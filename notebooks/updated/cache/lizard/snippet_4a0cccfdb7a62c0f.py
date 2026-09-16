def extract_features(self, dataset, missing_value_action='auto'):
    _raise_error_if_not_sframe(dataset, 'dataset')
    if missing_value_action == 'auto':
        missing_value_action = select_default_missing_value_policy(self,
            'extract_features')
    return self.__proxy__.extract_features(dataset, missing_value_action)