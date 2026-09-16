def get_resource_id(self):
    if not bool(self._my_map['resourceId']):
        raise errors.IllegalState('this Authorization has no resource')
    else:
        return Id(self._my_map['resourceId'])