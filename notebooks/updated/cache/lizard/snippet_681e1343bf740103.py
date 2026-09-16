def classname(self):
    if inspect.isclass(self):
        string = str(self)
    else:
        string = str(type(self))
    try:
        string = string.split("'")[1]
    except IndexError:
        pass
    return string.split('.')[-1]