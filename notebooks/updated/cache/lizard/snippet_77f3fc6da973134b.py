def get_extensions(self, data=False):
    ext_list = [key for key in self.__dict__ if type(self.__dict__[key]) is
        Extension]
    for key in ext_list:
        if data:
            yield getattr(self, key)
        else:
            yield key