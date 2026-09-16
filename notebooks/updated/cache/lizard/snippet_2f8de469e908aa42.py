def insert(self, data, return_object=False):
    obj = self(data)
    obj.save()
    if return_object:
        return obj
    else:
        return obj['_id']