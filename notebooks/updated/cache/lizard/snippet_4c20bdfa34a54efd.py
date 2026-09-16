def get_text(self, locator):
    text = self._get_text(locator)
    self._info("Element '%s' text is '%s' " % (locator, text))
    return text