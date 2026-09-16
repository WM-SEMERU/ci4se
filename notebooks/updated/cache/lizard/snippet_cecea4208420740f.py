def get_lowest_numeric_score_metadata(self):
    metadata = dict(self._mdata['lowest_numeric_score'])
    metadata.update({'existing_decimal_values': self._my_map[
        'lowestNumericScore']})
    return Metadata(**metadata)