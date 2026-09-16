def function_table(self, function_id=None):
    self._check_connected()
    function_table_keys = self.redis_client.keys(ray.gcs_utils.
        FUNCTION_PREFIX + '*')
    results = {}
    for key in function_table_keys:
        info = self.redis_client.hgetall(key)
        function_info_parsed = {'DriverID': binary_to_hex(info[b'driver_id'
            ]), 'Module': decode(info[b'module']), 'Name': decode(info[
            b'name'])}
        results[binary_to_hex(info[b'function_id'])] = function_info_parsed
    return results