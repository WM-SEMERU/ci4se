def _SyncAttributes(self):
    for attribute, value_array in iteritems(self.new_attributes):
        if not attribute.versioned or self.age_policy == NEWEST_TIME:
            value = value_array[-1]
            self.synced_attributes[attribute] = [LazyDecoder(decoded=value,
                age=value.age)]
        else:
            synced_value_array = self.synced_attributes.setdefault(attribute,
                [])
            for value in value_array:
                synced_value_array.append(LazyDecoder(decoded=value, age=
                    value.age))
            synced_value_array.sort(key=lambda x: x.age, reverse=True)
    self.new_attributes = {}
    self._to_delete.clear()
    self._dirty = False
    self._new_version = False