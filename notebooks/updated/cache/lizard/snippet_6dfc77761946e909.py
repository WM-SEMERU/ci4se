def verify(self, obj):
    if obj is not None:
        raise ValidationError('Object is not None', reason='%s is not None' %
            str(obj), object=obj)
    return obj