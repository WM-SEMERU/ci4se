def get_distribute_alterations_metadata(self):
    metadata = dict(self._mdata['distribute_alterations'])
    metadata.update({'existing_boolean_values': self._my_map[
        'distributeAlterations']})
    return Metadata(**metadata)