def column(self, model=None):
    try:
        schema = (self.__model or model).schema()
    except AttributeError:
        return None
    else:
        return schema.column(self.__column)