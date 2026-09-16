def get_datatype_str(self, element, length):
    spaces = ' ' * (self.get_width(element) - length)
    type_info = element.get('type')
    ret = ''
    if type_info == 'anyxml' or type_info == 'anydata':
        ret = spaces + '<{}>'.format(type_info)
    elif element.get('datatype') is not None:
        ret = spaces + element.get('datatype')
    if element.get('if-feature') is not None:
        return ret + ' {' + element.get('if-feature') + '}?'
    else:
        return ret