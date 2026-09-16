def wait_until_page_does_not_contain_element(self, locator, timeout=None,
    error=None):

    def check_present():
        present = self._is_element_present(locator)
        if not present:
            return
        else:
            return error or "Element '%s' did not disappear in %s" % (locator,
                self._format_timeout(timeout))
    self._wait_until_no_error(timeout, check_present)