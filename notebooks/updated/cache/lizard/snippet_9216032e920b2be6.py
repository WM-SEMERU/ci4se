def vars_(self):
    return [x for x in self[self.current_scope].values() if x.class_ ==
        CLASS.var]