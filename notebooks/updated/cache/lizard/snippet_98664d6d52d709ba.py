def linked_attribute(self):
    if isinstance(self.to_cls, str):
        return 'id'
    else:
        return self.via or self.to_cls.meta_.id_field.attribute_name