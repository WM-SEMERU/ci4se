def get_current_structure(self):
    struct = self.__class__.get_structure()
    struct.update(self.__field_types__)
    return struct