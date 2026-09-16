def get_qualifier_id(self):
    if not bool(self._my_map['qualifierId']):
        raise errors.IllegalState('qualifier empty')
    return Id(self._my_map['qualifierId'])