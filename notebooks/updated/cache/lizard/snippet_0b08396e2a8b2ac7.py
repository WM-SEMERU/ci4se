def find_first_object(self, ObjectClass, **kwargs):
    print('dynamo.find_first_object(%s, %s)' % (ObjectClass, str(kwargs)))
    query = self.db.engine.query(ObjectClass)
    for field_name, field_value in kwargs.items():
        field = getattr(ObjectClass, field_name, None)
        if field is None:
            raise KeyError(
                "DynamoDBAdapter.find_first_object(): Class '%s' has no field '%s'."
                 % (ObjectClass, field_name))
        query = query.filter(field == field_value)
    out = query.first(desc=True)
    return out