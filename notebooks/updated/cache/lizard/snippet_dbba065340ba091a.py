def get_values_by_type(self, type_p, which):
    if not isinstance(type_p, VirtualSystemDescriptionType):
        raise TypeError(
            'type_p can only be an instance of type VirtualSystemDescriptionType'
            )
    if not isinstance(which, VirtualSystemDescriptionValueType):
        raise TypeError(
            'which can only be an instance of type VirtualSystemDescriptionValueType'
            )
    values = self._call('getValuesByType', in_p=[type_p, which])
    return values