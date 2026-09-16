def get(self, model, **spec):
    handles = self.__find_handles(model, **spec)
    if len(handles) > 1:
        raise MultipleObjectsReturned()
    if not handles:
        raise ObjectDoesNotExist()
    return self.get_instance(model, handles[0])