def _create_visual_content_element(self, content, data_property_value):
    content_element = self._create_content_element(content, data_property_value
        )
    content_element.set_attribute('aria-hidden', 'true')
    content_element.set_attribute('role', 'presentation')
    return content_element