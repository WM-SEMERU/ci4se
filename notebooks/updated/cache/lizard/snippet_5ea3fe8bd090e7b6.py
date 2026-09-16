def is_element_available(self, locator):
    if self.driver.is_element_present(locator):
        if self.driver.is_visible(locator):
            return True
        else:
            return False
    else:
        return False