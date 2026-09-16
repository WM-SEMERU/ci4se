def check_element(self, elem, check_children=False, next_to_elem=None):
    self.__add_element('eid', elem.attribs, self.__element_ids, elem,
        next_to_elem)
    self.__add_element('aid', elem.attribs, self.__attrib_ids, elem,
        next_to_elem)
    self.__add_element('rid', elem.attribs, self.__repeat_ids, elem,
        next_to_elem)
    if check_children and elem.children:
        for child in elem.children:
            self.check_element(child, True, next_to_elem)