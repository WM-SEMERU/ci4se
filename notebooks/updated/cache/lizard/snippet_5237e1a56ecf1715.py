def get_input_score_start_range_metadata(self):
    metadata = dict(self._mdata['input_score_start_range'])
    metadata.update({'existing_decimal_values': self._my_map[
        'inputScoreStartRange']})
    return Metadata(**metadata)