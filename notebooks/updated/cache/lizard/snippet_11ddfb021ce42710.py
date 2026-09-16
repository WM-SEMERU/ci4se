def process_value(self, name, value, module_name):
    if ':' in name:
        if module_name.split(' ')[0] in I3S_MODULE_NAMES + ['general']:
            self.error('Only py3status modules can use obfuscated')
        if type(value).__name__ not in ['str', 'unicode']:
            self.error('Only strings can be obfuscated')
        name, scheme = name.split(':')
        if scheme == 'base64':
            value = PrivateBase64(value, module_name)
        elif scheme == 'hide':
            value = PrivateHide(value, module_name)
        else:
            self.error('Unknown scheme {} for data'.format(scheme))
    return name, value