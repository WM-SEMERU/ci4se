def child_elements(self, by=By.ID, value=None, el_class=None):
    el, selector = define_selector(by, value, el_class)
    return self._init_element(elements.PageElementsList(selector, el))