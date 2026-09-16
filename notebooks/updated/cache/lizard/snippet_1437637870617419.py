def aliases(self):
    return [x for x in self[self.current_scope].values() if x.is_aliased]