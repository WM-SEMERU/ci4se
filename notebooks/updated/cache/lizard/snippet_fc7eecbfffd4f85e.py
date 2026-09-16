def click_by_selector(self, selector):
    elem = find_element_by_jquery(world.browser, selector)
    elem.click()