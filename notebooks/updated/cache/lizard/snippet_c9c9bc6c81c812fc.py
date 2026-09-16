def save_form(self, form):
    force = self.get_force_instance_values()
    if force:
        for k, v in force.items():
            setattr(form.instance, k, v)
    should_add = False
    if self.parent_object:
        m2ms = [f.name for f in form.instance._meta.many_to_many]
        m2ms.extend([f.field.rel.related_name for f in [f for f in form.
            instance._meta.get_fields(include_hidden=True) if f.
            many_to_many and f.auto_created]])
        if self.parent_field in m2ms:
            should_add = True
        else:
            try:
                form.instance._meta.get_field(self.parent_field)
                setattr(form.instance, self.parent_field, self.parent_object)
            except FieldDoesNotExist:
                pass
    obj = form.save()
    if should_add:
        getattr(obj, self.parent_field).add(self.parent_object)
    return obj