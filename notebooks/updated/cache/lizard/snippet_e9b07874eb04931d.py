def to_dict(self):
    stage_desc_as_dict = {'uid': self._uid, 'name': self._name, 'state':
        self._state, 'state_history': self._state_history,
        'parent_pipeline': self._p_pipeline}
    return stage_desc_as_dict