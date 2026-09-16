def delete_app_id(self, app_id, mount_point='app-id'):
    return self._adapter.delete('/v1/auth/{0}/map/app-id/{1}'.format(
        mount_point, app_id))