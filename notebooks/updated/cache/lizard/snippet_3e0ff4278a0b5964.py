def _handle_class_instance(self, klass):
    if (klass in self.blacklisted_plugins or not self.instantiate_classes or
        klass == IPlugin):
        return
    elif self.unique_instances and self._unique_class(klass):
        self.plugins.append(klass())
    elif not self.unique_instances:
        self.plugins.append(klass())