def merge_entities(self, from_entity_ids, to_entity_id, force=False,
    mount_point=DEFAULT_MOUNT_POINT):
    params = {'from_entity_ids': from_entity_ids, 'to_entity_id':
        to_entity_id, 'force': force}
    api_path = '/v1/{mount_point}/entity/merge'.format(mount_point=mount_point)
    return self._adapter.post(url=api_path, json=params)