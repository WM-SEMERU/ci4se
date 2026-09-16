def element_background_color_should_be(self, locator, expected):
    self._info("Verifying element '%s' has background color '%s'" % (
        locator, expected))
    self._check_element_css_value(locator, 'background-color', expected)