def _validate(self):
    if self._state is not states.INITIAL:
        raise ValueError(obj=self._uid, attribute='state', expected_value=
            states.INITIAL, actual_value=self._state)
    if not self._executable:
        raise MissingError(obj=self._uid, missing_attribute='executable')