def deserialize(self, value, **kwargs):
    kwargs.update({'trusted': kwargs.get('trusted', False)})
    if self.deserializer is not None:
        return self.deserializer(value, **kwargs)
    if value is None:
        return None
    output_list = [self.prop.deserialize(val, **kwargs) for val in value]
    return self._class_container(output_list)