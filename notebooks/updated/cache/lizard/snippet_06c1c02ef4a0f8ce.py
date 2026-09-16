def find_elements(self, by=By.ID, value=None, el_class=None):
    els = self.child_elements(by, value, el_class)
    els.reload()
    return els