def represent_bool(self, data):
    if data:
        value = 'yes'
    else:
        value = 'no'
    return self.represent_scalar('tag:yaml.org,2002:bool', value)