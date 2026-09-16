def find_one(self, spec_or_id, **kwargs):
    if spec_or_id is not None and not isinstance(spec_or_id, dict):
        spec_or_id = {'_id': spec_or_id}
    kwargs['limit'] = -1
    self.find(spec_or_id, **kwargs)