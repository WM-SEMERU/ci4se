def get_rating_metadata(self):
    metadata = dict(self._mdata['rating'])
    metadata.update({'existing_id_values': self._my_map['ratingId']})
    return Metadata(**metadata)