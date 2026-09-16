def apply_strategy(self):
    method_id = self.conf.strategy.replace('-', '_')
    if not hasattr(DuplicateSet, method_id):
        raise NotImplementedError('DuplicateSet.{}() method.'.format(method_id)
            )
    return getattr(self, method_id)()