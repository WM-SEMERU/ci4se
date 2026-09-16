def delete_entity_alias(self, alias_id, mount_point=DEFAULT_MOUNT_POINT):
    api_path = '/v1/{mount_point}/entity-alias/id/{id}'.format(mount_point=
        mount_point, id=alias_id)
    return self._adapter.delete(url=api_path)