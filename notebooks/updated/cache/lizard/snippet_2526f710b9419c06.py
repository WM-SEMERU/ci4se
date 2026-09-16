def _clone(self, deepcopy=True, base=None):
    if not base:
        if self.__explicit_session:
            base = self._clone_base(self.__session)
        else:
            base = self._clone_base(None)
    values_to_clone = ('spec', 'projection', 'skip', 'limit', 'max_time_ms',
        'max_await_time_ms', 'comment', 'max', 'min', 'ordering', 'explain',
        'hint', 'batch_size', 'max_scan', 'manipulate', 'query_flags',
        'modifiers', 'collation')
    data = dict((k, v) for k, v in iteritems(self.__dict__) if k.startswith
        ('_Cursor__') and k[9:] in values_to_clone)
    if deepcopy:
        data = self._deepcopy(data)
    base.__dict__.update(data)
    return base