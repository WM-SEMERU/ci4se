def get_published_metadata(self):
    metadata = dict(self._mdata['published'])
    metadata.update({'existing_boolean_values': self._my_map['published']})
    return Metadata(**metadata)