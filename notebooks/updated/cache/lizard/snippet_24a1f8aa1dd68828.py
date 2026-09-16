def save(self, to_save, **kwargs):
    check = kwargs.pop('check', True)
    if check:
        self._valid_record(to_save)
    if '_id' in to_save:
        self.__collect.replace_one({'_id': to_save['_id']}, to_save, **kwargs)
        return to_save['_id']
    else:
        result = self.__collect.insert_one(to_save, **kwargs)
        return result.inserted_id