def wait_until_element_has_focus(self, locator, timeout=None):
    self._info("Waiting for focus on '%s'" % locator)
    self._wait_until_no_error(timeout, self._check_element_focus_exp, True,
        locator, timeout)