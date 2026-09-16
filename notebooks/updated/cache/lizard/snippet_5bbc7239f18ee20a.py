def get_string_resources(self, package_name, locale='\x00\x00'):
    self._analyse()
    buff = '<?xml version="1.0" encoding="utf-8"?>\n'
    buff += '<resources>\n'
    try:
        for i in self.values[package_name][locale]['string']:
            if any(map(i[1].__contains__, '<&>')):
                value = '<![CDATA[%s]]>' % i[1]
            else:
                value = i[1]
            buff += '<string name="{}">{}</string>\n'.format(i[0], value)
    except KeyError:
        pass
    buff += '</resources>\n'
    return buff.encode('utf-8')