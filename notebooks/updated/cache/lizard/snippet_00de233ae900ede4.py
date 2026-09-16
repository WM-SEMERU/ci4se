def get_width(self, element):
    parent = element.getparent()
    if parent in self.width:
        return self.width[parent]
    ret = 0
    for sibling in parent.getchildren():
        w = len(self.get_name_str(sibling))
        if w > ret:
            ret = w
    self.width[parent] = math.ceil((ret + 3) / 3.0) * 3
    return self.width[parent]