def _contains_policies(self, resource_properties):
    return resource_properties is not None and isinstance(resource_properties,
        dict) and self.POLICIES_PROPERTY_NAME in resource_properties