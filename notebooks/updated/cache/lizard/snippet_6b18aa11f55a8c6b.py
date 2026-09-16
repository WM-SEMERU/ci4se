def _get_class_repo(self, namespace):
    self._validate_namespace(namespace)
    if namespace not in self.classes:
        self.classes[namespace] = NocaseDict()
    return self.classes[namespace]