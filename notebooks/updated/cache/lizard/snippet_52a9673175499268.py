def transitions(self, current=True):
    if current and isinstance(self.obj, RoleMixin):
        proxy = self.obj.current_access()
    else:
        proxy = {}
        current = False
    return OrderedDict((name, transition) for name, transition in ((name,
        getattr(self.obj, name)) for name in self.statemanager.transitions) if
        transition.is_available and (name in proxy if current else True))