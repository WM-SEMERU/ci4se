def _generate_resource_dict(self):
    resource_dict = {}
    resource_dict['Type'] = self.resource_type
    if self.depends_on:
        resource_dict['DependsOn'] = self.depends_on
    resource_dict.update(self.resource_attributes)
    properties_dict = {}
    for name in self.property_types:
        value = getattr(self, name)
        if value is not None:
            properties_dict[name] = value
    resource_dict['Properties'] = properties_dict
    return resource_dict