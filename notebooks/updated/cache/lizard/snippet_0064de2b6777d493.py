def update(self, options=None, attribute_options=None):
    attr_map = self.__get_attribute_map(self.__mapped_cls, None, 0)
    for attributes in attribute_options:
        for attr_name in attributes:
            if not attr_name in attr_map:
                raise AttributeError(
                    'Trying to configure non-existing resource attribute "%s"'
                     % attr_name)
    cfg = RepresenterConfiguration(options=options, attribute_options=
        attribute_options)
    self.configuration.update(cfg)