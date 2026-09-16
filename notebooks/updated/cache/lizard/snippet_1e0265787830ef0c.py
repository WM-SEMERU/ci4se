def _find_by_nsp(self, browser, criteria, tag, constraints):
    return self._filter_elements(browser.find_elements_by_ios_predicate(
        criteria), tag, constraints)