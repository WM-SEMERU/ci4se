def assert_visible(self, locator, msg=None):
    e = driver.find_elements_by_locator(locator)
    if len(e) == 0:
        raise AssertionError('Element at %s was not found' % locator)
    assert e.is_displayed()