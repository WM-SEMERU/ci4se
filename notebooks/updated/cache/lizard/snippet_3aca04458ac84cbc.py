def _apply_scope(self, scope, builder):
    if callable(scope):
        scope(builder)
    elif isinstance(scope, Scope):
        scope.apply(builder, self.get_model())