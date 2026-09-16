def add_filter(self, entry):
    entry = entry[10:-1]
    info = entry.split(',')
    if len(info) < 2:
        return False
    for v in info:
        key, value = v.split('=', 1)
        if key == 'ID':
            self.filter[value] = {}
            id_ = value
        elif key == 'Description':
            self.filter[id_]['description'] = value
            if len(info) > 2:
                self.info[id_]['description'] += '; '.join(info[2:])
    return True