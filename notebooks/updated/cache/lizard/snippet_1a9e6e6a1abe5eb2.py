def BackAssign(cls, other_entity_klass, this_entity_backpopulate_field,
    other_entity_backpopulate_field, is_many_to_one=False):
    data = dict()
    for _, other_klass in other_entity_klass.Subclasses():
        other_field_value = getattr(other_klass, this_entity_backpopulate_field
            )
        if isinstance(other_field_value, (tuple, list)):
            for self_klass in other_field_value:
                self_key = self_klass.__name__
                try:
                    data[self_key].append(other_klass)
                except KeyError:
                    data[self_key] = [other_klass]
        elif other_field_value is not None:
            self_klass = other_field_value
            self_key = self_klass.__name__
            try:
                data[self_key].append(other_klass)
            except KeyError:
                data[self_key] = [other_klass]
    if is_many_to_one:
        new_data = dict()
        for key, value in data.items():
            try:
                new_data[key] = value[0]
            except:
                pass
        data = new_data
    for self_key, other_klass_list in data.items():
        setattr(getattr(cls, self_key), other_entity_backpopulate_field,
            other_klass_list)