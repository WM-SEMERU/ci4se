def remove_callback(self, name, callback):
    if self.is_callback_property(name):
        prop = getattr(type(self), name)
        try:
            prop.remove_callback(self, callback)
        except ValueError:
            pass
    else:
        raise TypeError("attribute '{0}' is not a callback property".format
            (name))