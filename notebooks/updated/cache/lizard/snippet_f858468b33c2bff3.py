def is_visible(self, selector):
    self.debug_log('Is visible (%s)' % selector)
    element = self.find(selector, raise_exception=False, wait_until_present
        =False, wait_until_visible=False)
    if element:
        if element.is_displayed(raise_exception=False):
            element.highlight(style=BROME_CONFIG['highlight'][
                'element_is_visible'])
            self.debug_log('is visible (%s): True' % selector)
            return True
    self.debug_log('is visible (%s): False' % selector)
    return False