def register_class(self, class_type, component_scope=scope.
    InstancePerDependency, register_as=None):
    registration = _ConstructorRegistration(class_type, component_scope())
    self._register(class_type, registration, register_as)