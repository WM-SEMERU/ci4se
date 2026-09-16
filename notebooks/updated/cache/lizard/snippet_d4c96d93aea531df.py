def get_element_location(self, locator):
    element = self._element_find(locator, True, True)
    element_location = element.location
    self._info("Element '%s' location: %s " % (locator, element_location))
    return element_location