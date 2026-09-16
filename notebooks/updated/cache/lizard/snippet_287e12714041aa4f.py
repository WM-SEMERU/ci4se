def restore_model(cls, data):
    obj = cls()
    for field in data:
        setattr(obj, field, data[field][Field.VALUE])
    return obj