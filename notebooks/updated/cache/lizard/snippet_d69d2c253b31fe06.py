def get_description_metadata(self):
    metadata = dict(self._mdata['description'])
    metadata.update({'existing_string_values': self._my_map['description'][
        'text']})
    return Metadata(**metadata)