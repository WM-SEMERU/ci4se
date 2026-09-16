def enter(self, screen_id, y, x, default_action, allowed_actions, formats):
    if not isinstance(screen_id, baseinteger):
        raise TypeError('screen_id can only be an instance of type baseinteger'
            )
    if not isinstance(y, baseinteger):
        raise TypeError('y can only be an instance of type baseinteger')
    if not isinstance(x, baseinteger):
        raise TypeError('x can only be an instance of type baseinteger')
    if not isinstance(default_action, DnDAction):
        raise TypeError(
            'default_action can only be an instance of type DnDAction')
    if not isinstance(allowed_actions, list):
        raise TypeError('allowed_actions can only be an instance of type list')
    for a in allowed_actions[:10]:
        if not isinstance(a, DnDAction):
            raise TypeError('array can only contain objects of type DnDAction')
    if not isinstance(formats, list):
        raise TypeError('formats can only be an instance of type list')
    for a in formats[:10]:
        if not isinstance(a, basestring):
            raise TypeError('array can only contain objects of type basestring'
                )
    result_action = self._call('enter', in_p=[screen_id, y, x,
        default_action, allowed_actions, formats])
    result_action = DnDAction(result_action)
    return result_action