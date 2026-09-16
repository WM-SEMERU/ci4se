def show(self):
    bytecode._PrintSubBanner('Field Information')
    bytecode._PrintDefault('{}->{} {} [access_flags={}]\n'.format(self.
        get_class_name(), self.get_name(), self.get_descriptor(), self.
        get_access_flags_string()))
    init_value = self.get_init_value()
    if init_value is not None:
        bytecode._PrintDefault('\tinit value: %s\n' % str(init_value.
            get_value()))