def element_focus_should_not_be_set(self, locator):
    self._info("Verifying element '%s' focus is not set" % locator)
    self._check_element_focus(False, locator)