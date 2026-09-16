def drop(self, format_p, action):
    if not isinstance(format_p, basestring):
        raise TypeError('format_p can only be an instance of type basestring')
    if not isinstance(action, DnDAction):
        raise TypeError('action can only be an instance of type DnDAction')
    progress = self._call('drop', in_p=[format_p, action])
    progress = IProgress(progress)
    return progress