def recordset(method):

    def wrapper(self, *args, **kwargs):
        if self.__records__ is None:
            raise ValidationError('There are no records in the set.')
        return method(self, *args, **kwargs)
    return Api.model(wrapper)