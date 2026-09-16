def to_dict(self):
    return {'all_set': self._is_all_set(), 'progress': self.progress(),
        'values': {property_name: (getattr(self, property_name) or []) for
        property_name in worker_mapping().keys()}}