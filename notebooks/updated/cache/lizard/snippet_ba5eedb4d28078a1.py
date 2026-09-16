def put(self, key, value):
    if key == None or key == '':
        return None
    elif key.find('.') > 0:
        RecursiveObjectWriter.set_property(self, key, value)
        return value
    else:
        self[key] = value
        return value