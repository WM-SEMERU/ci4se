def get_enum(self, property, enum, datas):
    str_property = str(datas[property]).lower()
    if str_property not in enum:
        raise ValueError('Unknow enum "%s" for "%s".' % (str_property,
            property))
    return enum(str_property)