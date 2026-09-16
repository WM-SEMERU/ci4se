def _faster_to_representation(self, instance):
    ret = {}
    fields = self._readable_fields
    is_fast = isinstance(instance, prefetch.FastObject)
    id_fields = self._readable_id_fields
    for field in fields:
        attribute = None
        if is_fast and not isinstance(field, (DynamicGenericRelationField,
            DynamicRelationField)):
            if field in id_fields and field.source not in instance:
                attribute = instance.get(field.source + '_id')
                ret[field.field_name] = attribute
                continue
            else:
                try:
                    attribute = instance[field.source]
                except KeyError:
                    if hasattr(instance, field.source):
                        attribute = getattr(instance, field.source)
                    else:
                        attribute = field.get_attribute(instance)
                        print('Missing %s from %s' % (field.field_name,
                            self.__class__.__name__))
        else:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue
        if attribute is None:
            ret[field.field_name] = None
        else:
            ret[field.field_name] = field.to_representation(attribute)
    return ret