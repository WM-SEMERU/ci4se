def meta(self, type):
    try:
        return self.registered_formats[type].get('meta')
    except KeyError:
        raise NotImplementedError("No format registered with type '{type}'"
            .format(type=type))