def adapter(self, adapter):
    self._adapter = adapter
    for implemented_class in self.implemented_classes:
        class_name = implemented_class.__name__.lower()
        getattr(self, self.get_private_attr_name(class_name)).adapter = adapter