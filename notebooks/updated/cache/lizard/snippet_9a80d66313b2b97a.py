def set(self, instance, value, **kwargs):
    val = get_date(instance, value)
    super(DateTimeField, self).set(instance, val, **kwargs)