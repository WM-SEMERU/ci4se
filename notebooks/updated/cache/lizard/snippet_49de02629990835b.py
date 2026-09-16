def visit_and_update_expressions(self, visitor_fn):
    new_fields = {}
    for key, value in six.iteritems(self.fields):
        new_value = value.visit_and_update(visitor_fn)
        if new_value is not value:
            new_fields[key] = new_value
    if new_fields:
        return ConstructResult(dict(self.fields, **new_fields))
    else:
        return self