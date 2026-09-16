def _deserialize(self, value, attr, data):
    return super(DateString, self)._deserialize(value, attr, data).isoformat()