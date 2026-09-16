def find_first_object(self, ObjectClass, **kwargs):
    query = ObjectClass.query
    for field_name, field_value in kwargs.items():
        field = getattr(ObjectClass, field_name, None)
        if field is None:
            raise KeyError(
                "BaseAlchemyAdapter.find_first_object(): Class '%s' has no field '%s'."
                 % (ObjectClass, field_name))
        query = query.filter(field == field_value)
    return query.first()