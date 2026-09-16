def get_object(self, resource_url):
    if resource_url in self.cache:
        cache_id = self.cache[resource_url]
    else:
        cache_id = str(uuid.uuid4())
    obj_dir = os.path.join(self.directory, cache_id)
    f_json = os.path.join(obj_dir, '.json')
    is_active = True
    try:
        obj_json = sco.JsonResource(resource_url).json
        if not os.path.isdir(obj_dir):
            os.mkdir(obj_dir)
        with open(f_json, 'w') as f:
            json.dump(obj_json, f)
    except ValueError as ex:
        if os.path.isfile(f_json):
            with open(f_json, 'r') as f:
                obj_json = json.load(f)
            is_active = False
        else:
            raise ex
    return obj_dir, obj_json, is_active, cache_id