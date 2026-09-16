def create_default_element(self, name):
    found = self.root.find(name)
    if found is not None:
        return found
    ele = ET.Element(name)
    self.root.append(ele)
    return ele