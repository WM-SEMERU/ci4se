def container(self, name, length, type, *parameters):
    self.new_struct('Container', name, 'length=%s' % length)
    BuiltIn().run_keyword(type, *parameters)
    self.end_struct()