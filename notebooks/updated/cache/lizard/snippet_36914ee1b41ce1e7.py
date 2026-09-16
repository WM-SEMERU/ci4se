def from_python(self, value):
    if isinstance(value, model.RedisModel):
        value = value._pk
    elif isinstance(value, SimpleValueRelatedFieldMixin):
        value = value.proxy_get()
    return value