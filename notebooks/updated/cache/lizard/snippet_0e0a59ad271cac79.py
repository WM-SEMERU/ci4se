def get_present_element(self, locator, params=None, timeout=None, visible=
    False, parent=None):
    error_msg = ('Child was never present' if parent else
        'Element was never present!')
    expected_condition = (ec.visibility_of_element_located if visible else
        ec.presence_of_element_located)
    return self._get(locator, expected_condition, params, timeout,
        error_msg, parent)