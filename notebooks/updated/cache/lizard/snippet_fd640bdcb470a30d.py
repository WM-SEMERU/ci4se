def element(self, *args, **kwargs):
    child_element = self._element.add_element(*args, **kwargs)
    return Builder(child_element)