def get_timestamp_metadata(self):
    metadata = dict(self._mdata['timestamp'])
    metadata.update({'existing_date_time_values': self._my_map['timestamp']})
    return Metadata(**metadata)