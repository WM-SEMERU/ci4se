def format(self, rev_id=None, model_name=None):
    rev_ids = rev_id if rev_id is not None else set(self.rev_ids)
    model_names = model_name if model_name is not None else set(self.
        model_names)
    common = [self.context_name, rev_ids, model_names]
    optional = []
    if self.precache:
        optional.append('precache')
    if self.include_features:
        optional.append('features')
    if self.injection_caches:
        optional.append('injection_caches={0}'.format(self.injection_caches))
    if self.model_info:
        optional.append('model_info=' + json.dumps(self.model_info))
    if self.ip:
        optional.append('ip={0}'.format(self.ip))
    return '{0}({1})'.format(':'.join(repr(v) for v in common), ', '.join(
        optional))