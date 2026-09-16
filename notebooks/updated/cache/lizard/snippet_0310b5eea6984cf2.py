def set_incoming(self, value):
    if not isinstance(value, list):
        raise TypeError('IncomingList new value must be a list')
    for element in value:
        if not isinstance(element, str):
            raise TypeError(
                'IncomingList elements in variable must be of String class')
    self.__incoming_list = value