def permitted_actions(self, obj=None):
    return [a for a in Action.registered if self.allow(a, obj(str(a)) if 
        obj is not None else None)]