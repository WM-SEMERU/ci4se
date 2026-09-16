def CreatedField(name='created', tz_aware=False, **kwargs):

    @computed_field(DateTimeField(), one_time=True, **kwargs)
    def created(obj):
        if tz_aware:
            import pytz
            return pytz.utc.localize(datetime.utcnow())
        return datetime.utcnow()
    created.__name__ = name
    return created