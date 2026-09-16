def element_focus_should_be_set(self, locator):
    self._info("Verifying element '%s' focus is set" % locator)
    self._check_element_focus(True, locator)