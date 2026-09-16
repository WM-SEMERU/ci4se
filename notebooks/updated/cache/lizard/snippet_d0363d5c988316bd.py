def serialize(self, data):
    if data is None:
        return None
    elif isinstance(data, dict):
        return serializer.Serializer().serialize(data)
    else:
        raise Exception(_("Unable to serialize object of type = '%s'") %
            type(data))