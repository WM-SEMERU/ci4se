def load(self, file):
    if isfile(file):
        try:
            config = load_source('config', file)
        except Exception as e:
            raise ExceptionInConfigError(e)
        option_missing = False
        values = {}
        for option in self.options:
            if option.name not in dir(config):
                values[option.name] = option.default_value
                option_missing = True
            else:
                value = getattr(config, option.name)
                if option.validator != None:
                    if not option.validator(value):
                        values[option.name] = option.default_value
                        if self.validation_failed != None:
                            self.validation_failed(option.name, value)
                        else:
                            raise ValidationError(option.name)
                        option_missing = True
                    else:
                        values[option.name] = value
                else:
                    values[option.name] = value
            if option_missing:
                self.dump(file)
        return _EditableConfig(values, self.options, file,
            validation_failed=self.validation_failed, debug=self.debug)
    else:
        error = "'%s' not found" % file
        raise (FileNotFoundError(error) if version.startswith('3') else
            IOError(error))