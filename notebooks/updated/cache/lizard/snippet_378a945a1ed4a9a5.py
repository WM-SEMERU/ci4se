def _serialize(self, value, attr, obj):
    if value is None:
        return None
    if self.use_isoformat:
        return datetime.utcfromtimestamp(value).isoformat()
    else:
        return value