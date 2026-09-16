def is_correct(self):
    state = True
    cls = self.__class__
    if not self.notificationways:
        for prop in self.special_properties:
            if not hasattr(self, prop):
                msg = '[contact::%s] %s property is missing' % (self.
                    get_name(), prop)
                self.add_error(msg)
                state = False
    if not hasattr(self, 'contact_name'):
        if hasattr(self, 'alias'):
            self.contact_name = self.alias
    for char in cls.illegal_object_name_chars:
        if char not in self.contact_name:
            continue
        msg = '[contact::%s] %s character not allowed in contact_name' % (self
            .get_name(), char)
        self.add_error(msg)
        state = False
    return super(Contact, self).is_correct() and state