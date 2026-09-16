def actions(self, context=None):
    assert self.installed(), 'Actions not enabled on this application'
    result = {}
    if context is None:
        context = self.context
    for cat, actions in self._state['categories'].items():
        result[cat] = [a for a in actions if a.available(context)]
    return result