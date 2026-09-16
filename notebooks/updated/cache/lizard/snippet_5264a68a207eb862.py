def get(self, sent_id, **kwargs):
    if sent_id is not None and not isinstance(sent_id, int):
        sent_id = int(sent_id)
    if sent_id is None or not self.has_id(sent_id):
        if 'default' in kwargs:
            return kwargs['default']
        else:
            raise KeyError('Invalid sentence ID ({})'.format(sent_id))
    return self.__sent_map[sent_id]