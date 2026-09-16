def attr(self, attr_name, attr_value=None):
    name = self.__attr_name(attr_name)
    if attr_value is not None:
        if WHTTPCookie.cookie_attr_value_check(name, attr_value) is not True:
            raise ValueError('Unacceptable value passed')
        if self.__ro_flag:
            raise RuntimeError('Read-only cookie changing attempt')
        self.__attrs[name] = attr_value
        return attr_value
    return self.__attrs[name]