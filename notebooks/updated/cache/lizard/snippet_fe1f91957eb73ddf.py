def on_show_window(self, check):
    if not isinstance(check, bool):
        raise TypeError('check can only be an instance of type bool')
    can_show, win_id = self._call('onShowWindow', in_p=[check])
    return can_show, win_id