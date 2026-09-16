def is_present(self, selector):
    self.debug_log('Is present (%s)' % selector)
    element = self.find(selector, raise_exception=False, wait_until_present
        =False, wait_until_visible=False)
    if element:
        self.debug_log('is present: True')
        return True
    else:
        self.debug_log('is present: False')
        return False