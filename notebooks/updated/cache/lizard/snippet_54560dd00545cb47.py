def scope_choices(self, exclude_internal=True):
    return [(k, scope) for k, scope in sorted(self.scopes.items()) if not
        exclude_internal or not scope.is_internal]