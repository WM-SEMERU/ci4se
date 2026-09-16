def _initialize(self, **resource_attributes):
    self._set_attributes(**resource_attributes)
    for attribute, attribute_type in list(self._mapper.items()):
        if attribute in resource_attributes and isinstance(resource_attributes
            [attribute], dict):
            setattr(self, attribute, attribute_type(**resource_attributes[
                attribute]))