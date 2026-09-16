def get_source_id(self):
    if not bool(self._my_map['sourceId']):
        raise errors.IllegalState('this Asset has no source')
    else:
        return Id(self._my_map['sourceId'])