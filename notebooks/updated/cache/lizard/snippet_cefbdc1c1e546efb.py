def execute_resource_async(self, device_id, resource_path, fix_path=True):
    if not resource_path.startswith('/'):
        resource_path = '/' + resource_path
    return self._mds_rpc_post(device_id=device_id, method='POST', uri=
        resource_path)