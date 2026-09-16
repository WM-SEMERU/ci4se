def fill_data_brok_from(self, data, brok_type):
    cls = self.__class__
    for prop, entry in list(cls.properties.items()):
        if brok_type in entry.fill_brok:
            if hasattr(self, prop):
                data[prop] = getattr(self, prop)