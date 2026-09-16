def _rewrite_error_path(self, error, offset=0):
    if error.is_logic_error:
        self._rewrite_logic_error_path(error, offset)
    elif error.is_group_error:
        self._rewrite_group_error_path(error, offset)