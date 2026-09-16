def initialize_fields(self, content):
    for name, value in content.items():
        if name is 'value':
            self.value = value
        elif name is 'data':
            if is_mixin(self._data):
                self._data.initialize_fields(value)
            elif is_field(self._data):
                self._data.value = value