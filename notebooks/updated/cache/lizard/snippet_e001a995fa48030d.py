def new_scope(self, new_scope={}):
    old_scopes, self.scopes = self.scopes, self.scopes.new_child(new_scope)
    yield
    self.scopes = old_scopes