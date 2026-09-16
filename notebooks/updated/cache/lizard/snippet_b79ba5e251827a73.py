def set_path(self, data, path, value):
    self.say('set_path:value:' + str(value) + ' at:' + str(path) + ' in:' +
        str(data))
    if isinstance(path, str):
        path = path.split('.')
    if len(path) > 1:
        self.set_path(data.setdefault(path[0], {}), path[1:], value)
    else:
        data[path[0]] = value
    return data