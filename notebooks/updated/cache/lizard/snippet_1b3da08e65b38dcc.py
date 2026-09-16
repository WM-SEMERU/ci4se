def to_yaml(self, str_or_buffer=None):
    logger.debug('serializing segmented LCM {} to YAML'.format(self.name))
    return yamlio.convert_to_yaml(self.to_dict(), str_or_buffer)