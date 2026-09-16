def drag_is_pending(self, screen_id):
    if not isinstance(screen_id, baseinteger):
        raise TypeError('screen_id can only be an instance of type baseinteger'
            )
    default_action, formats, allowed_actions = self._call('dragIsPending',
        in_p=[screen_id])
    default_action = DnDAction(default_action)
    allowed_actions = [DnDAction(a) for a in allowed_actions]
    return default_action, formats, allowed_actions