def register(self, key_or_tag, obj):
    if key_or_tag == 'default_decoder':
        self.options['default_decoder'] = obj
    else:
        self.decoders[key_or_tag] = obj