def info(self):
    itext = self.class_info
    if self.key_prop.info and self.value_prop.info:
        itext += ' (keys: {}; values: {})'.format(self.key_prop.info, self.
            value_prop.info)
    elif self.key_prop.info:
        itext += ' (keys: {})'.format(self.key_prop.info)
    elif self.value_prop.info:
        itext += ' (values: {})'.format(self.value_prop.info)
    return itext