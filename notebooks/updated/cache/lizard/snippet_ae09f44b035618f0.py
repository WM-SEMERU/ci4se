def remove_parameter(self, name):
    spec = self.__specs[name] if name in self.__specs else None
    if spec is not None and spec.optional() is False:
        raise ValueError('Unable to remove a required parameter "%s"' % name)
    WURIQuery.remove_parameter(self, name)