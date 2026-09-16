def get_converter(self, parameter):
    if parameter not in self._converters:
        param = self.get_parameter(parameter)
        try:
            scale = float(param['Scale'])
        except KeyError:
            scale = 1

        def convert(value):
            return value * scale
        return convert