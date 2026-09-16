def get_provider_metadata(self):
    metadata = dict(self._provider_metadata)
    metadata.update({'existing_id_values': self.my_osid_object_form._my_map
        ['providerId']})
    return Metadata(**metadata)