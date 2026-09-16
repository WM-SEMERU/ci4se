def release_attributes(self, attributes, active=True):
    attribute_update = self._post_object(self.update_api.attributes.release,
        attributes)
    return ExistAttributeResponse(attribute_update)