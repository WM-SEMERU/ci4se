def reprioritize(self, priority, element):
    if element not in self.element_finder:
        raise ValueError('No such element in the priority queue.')
    entry = self.element_finder[element]
    self.add_element(priority, element, entry[1])
    entry[1] = self.INVALID