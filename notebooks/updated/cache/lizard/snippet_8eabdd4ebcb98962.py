def get_element_size(self, locator):
    element = self._element_find(locator, True, True)
    element_size = element.size
    self._info("Element '%s' size: %s " % (locator, element_size))
    return element_size