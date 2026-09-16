def get_sections(self):
    try:
        obj_list = self.__dict__['sections']
        return [Section(i) for i in obj_list]
    except KeyError:
        self._lazy_load()
        obj_list = self.__dict__['sections']
        return [Section(i) for i in obj_list]