def add_type_conversion(self, start_type, target_type, conversion_function):
    self.registered_color_spaces.add(start_type)
    self.registered_color_spaces.add(target_type)
    logger.debug('Registered conversion from %s to %s', start_type, target_type
        )