def populate_obj_from_obj(self, instance, exclude_keys=None, include_keys=None
    ):
    exclude_keys_list = exclude_keys or []
    include_keys_list = include_keys or []
    for k in self._get_keys():
        if hasattr(instance, k) and k not in exclude_keys_list and (k in
            include_keys_list or not include_keys):
            setattr(self, k, getattr(instance, k))