def add_callback(self, name, callback, echo_old=False, priority=0):
    if self.is_callback_property(name):
        prop = getattr(type(self), name)
        prop.add_callback(self, callback, echo_old=echo_old, priority=priority)
    else:
        raise TypeError("attribute '{0}' is not a callback property".format
            (name))