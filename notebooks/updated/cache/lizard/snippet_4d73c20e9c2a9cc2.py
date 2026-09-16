def experiments_get(self, resource_url):
    obj_dir, obj_json, is_active, cache_id = self.get_object(resource_url)
    experiment = ExperimentHandle(obj_json, self)
    if not cache_id in self.cache:
        self.cache_add(resource_url, cache_id)
    return experiment