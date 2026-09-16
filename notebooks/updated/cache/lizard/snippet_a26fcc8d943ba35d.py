def _get_all_set_properties(self):
    return set(property_name for property_name in worker_mapping().keys() if
        getattr(self, property_name) is not None)