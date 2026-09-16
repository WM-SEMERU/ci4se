def element_type(self, type_):
    return self.__find_xxx_type(type_, self.element_type_index, self.
        element_type_typedef, 'container_element_type')