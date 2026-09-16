def get_unit_spike_features(self, unit_id, feature_name, start_frame=None,
    end_frame=None):
    if isinstance(unit_id, (int, np.integer)):
        if unit_id in self.get_unit_ids():
            if unit_id not in self._unit_features.keys():
                self._unit_features[unit_id] = {}
            if isinstance(feature_name, str):
                if feature_name in self._unit_features[unit_id].keys():
                    if start_frame is None:
                        start_frame = 0
                    if end_frame is None:
                        end_frame = len(self.get_unit_spike_train(unit_id))
                    return self._unit_features[unit_id][feature_name][
                        start_frame:end_frame]
                else:
                    raise ValueError(str(feature_name) +
                        ' has not been added to unit ' + str(unit_id))
            else:
                raise ValueError(str(feature_name) + ' must be a string')
        else:
            raise ValueError(str(unit_id) + ' is not a valid unit_id')
    else:
        raise ValueError(str(unit_id) + ' must be an int')