def created(self, data, schema=None, envelope=None):
    data = marshal(data, schema, envelope)
    return self.__make_response((data, 201))