def switch(self, name):
    try:
        switch = self.storage[self.__namespaced(name)]
    except KeyError:
        if not self.autocreate:
            raise ValueError("No switch named '%s' registered in '%s'" % (
                name, self.namespace))
        switch = self.__create_and_register_disabled_switch(name)
    switch.manager = self
    return switch