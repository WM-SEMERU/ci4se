def set_default_layouts(self, ignored_layouts=None):
    for key in self.__default_layouts_settings.allKeys():
        if ignored_layouts:
            if tuple(layout for layout in ignored_layouts if layout in key):
                continue
        self.__settings.setValue(key, self.__default_layouts_settings.value
            (key))
    return True