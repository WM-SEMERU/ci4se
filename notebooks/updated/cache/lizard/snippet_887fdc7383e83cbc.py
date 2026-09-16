def cache_key_exist(self, key):
    key_exist = True if cache.get(key) else False
    status = 200 if key_exist else 404
    return json_success(json.dumps({'key_exist': key_exist}), status=status)