def get_collection(self, **kwargs):
    list_of_contents = []
    self.refresh(**kwargs)
    if 'items' in self.__dict__:
        for item in self.items:
            if 'kind' not in item:
                list_of_contents.append(item)
                continue
            kind = item['kind']
            if kind in self._meta_data['attribute_registry']:
                instance = self._meta_data['attribute_registry'][kind](self)
                instance._local_update(item)
                instance._activate_URI(instance.selfLink)
                list_of_contents.append(instance)
            else:
                error_message = '%r is not registered!' % kind
                raise UnregisteredKind(error_message)
    return list_of_contents