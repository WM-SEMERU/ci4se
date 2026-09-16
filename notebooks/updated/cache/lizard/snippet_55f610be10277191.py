def get_rubric_metadata(self):
    metadata = dict(self._mdata['rubric'])
    metadata.update({'existing_id_values': self._my_map['rubricId']})
    return Metadata(**metadata)