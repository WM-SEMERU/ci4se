def get_end_date_metadata(self):
    metadata = dict(self._mdata['end_date'])
    metadata.update({'existing_date_time_values': self._my_map['endDate']})
    return Metadata(**metadata)